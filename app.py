from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS  # Temporarily commented out
import os
from werkzeug.utils import secure_filename
import PyPDF2
import pytesseract
from PIL import Image
import io
import re
from textstat import flesch_reading_ease, flesch_kincaid_grade
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import logging

# Download required NLTK data
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

app = Flask(__name__)
# CORS(app)  # Temporarily commented out

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    """Extract text from PDF file"""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise Exception(f"Failed to extract text from PDF: {str(e)}")

def extract_text_from_image(file_path):
    """Extract text from image using OCR"""
    try:
        image = Image.open(file_path)
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        logger.error(f"Error extracting text from image: {str(e)}")
        raise Exception(f"Failed to extract text from image: {str(e)}")

def analyze_content(text):
    """Analyze content and provide engagement suggestions"""
    try:
        # Basic text statistics
        word_count = len(text.split())
        char_count = len(text)
        sentence_count = len(re.findall(r'[.!?]+', text))
        
        # Readability scores
        try:
            readability = flesch_reading_ease(text)
            grade_level = flesch_kincaid_grade(text)
        except:
            readability = 0
            grade_level = 0
        
        # Sentiment analysis
        sentiment_scores = sia.polarity_scores(text)
        
        # Extract hashtags and mentions
        hashtags = re.findall(r'#\w+', text)
        mentions = re.findall(r'@\w+', text)
        
        # Common words (excluding common stop words)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
        common_words = Counter(filtered_words).most_common(10)
        
        # Generate suggestions
        suggestions = generate_engagement_suggestions(
            word_count, readability, sentiment_scores, hashtags, mentions, text
        )
        
        return {
            'statistics': {
                'word_count': word_count,
                'character_count': char_count,
                'sentence_count': sentence_count,
                'readability_score': round(readability, 2),
                'grade_level': round(grade_level, 2)
            },
            'sentiment': {
                'compound': round(sentiment_scores['compound'], 3),
                'positive': round(sentiment_scores['pos'], 3),
                'neutral': round(sentiment_scores['neu'], 3),
                'negative': round(sentiment_scores['neg'], 3),
                'overall': get_sentiment_label(sentiment_scores['compound'])
            },
            'social_elements': {
                'hashtags': hashtags,
                'mentions': mentions,
                'hashtag_count': len(hashtags),
                'mention_count': len(mentions)
            },
            'common_words': common_words,
            'suggestions': suggestions
        }
    except Exception as e:
        logger.error(f"Error analyzing content: {str(e)}")
        raise Exception(f"Failed to analyze content: {str(e)}")

def get_sentiment_label(compound_score):
    """Convert compound sentiment score to label"""
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def generate_engagement_suggestions(word_count, readability, sentiment_scores, hashtags, mentions, text):
    """Generate engagement improvement suggestions"""
    suggestions = []
    
    # Word count suggestions
    if word_count < 20:
        suggestions.append("Consider expanding your content - posts with 20-40 words tend to perform better")
    elif word_count > 100:
        suggestions.append("Your content is quite long - consider breaking it into shorter, more digestible posts")
    
    # Readability suggestions
    if readability < 30:
        suggestions.append("Your content is complex - try using simpler words and shorter sentences for better engagement")
    elif readability > 90:
        suggestions.append("Your content is very easy to read - great for broad audience engagement!")
    
    # Sentiment suggestions
    if sentiment_scores['compound'] < -0.3:
        suggestions.append("Consider adding more positive elements to balance the tone and improve engagement")
    elif sentiment_scores['compound'] > 0.3:
        suggestions.append("Great positive tone! This should resonate well with your audience")
    
    # Hashtag suggestions
    if len(hashtags) == 0:
        suggestions.append("Add relevant hashtags to increase discoverability (aim for 3-5 hashtags)")
    elif len(hashtags) > 10:
        suggestions.append("You're using many hashtags - consider reducing to 5-7 most relevant ones")
    
    # Call-to-action suggestions
    cta_patterns = r'\b(comment|share|like|follow|click|visit|check|try|buy|subscribe)\b'
    if not re.search(cta_patterns, text.lower()):
        suggestions.append("Add a call-to-action (e.g., 'What do you think?', 'Share your thoughts') to encourage engagement")
    
    # Question suggestions
    if '?' not in text:
        suggestions.append("Consider ending with a question to encourage comments and discussions")
    
    # Emoji suggestions (basic check)
    emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
    if not re.search(emoji_pattern, text):
        suggestions.append("Consider adding relevant emojis to make your post more visually appealing")
    
    if not suggestions:
        suggestions.append("Your content looks well-optimized for engagement!")
    
    return suggestions

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and analysis"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not supported. Please upload PDF or image files.'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text based on file type
        file_ext = filename.rsplit('.', 1)[1].lower()
        
        if file_ext == 'pdf':
            extracted_text = extract_text_from_pdf(file_path)
        else:
            extracted_text = extract_text_from_image(file_path)
        
        # Clean up uploaded file
        os.remove(file_path)
        
        if not extracted_text.strip():
            return jsonify({'error': 'No text could be extracted from the file'}), 400
        
        # Analyze the extracted text
        analysis_result = analyze_content(extracted_text)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'extracted_text': extracted_text,
            'analysis': analysis_result
        })
    
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/analyze', methods=['POST'])
def analyze_text():
    """Analyze text directly without file upload"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({'error': 'Empty text provided'}), 400
        
        # Analyze the text
        analysis_result = analyze_content(text)
        
        return jsonify({
            'success': True,
            'analysis': analysis_result
        })
    
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File too large. Maximum size is 16MB.'}), 413

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)