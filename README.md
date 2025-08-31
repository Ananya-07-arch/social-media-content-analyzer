# Social Media Content Analyzer

A web application that analyzes social media posts and suggests engagement improvements through document upload (PDF, images) or direct text input.

## Features

### 🔍 Content Analysis
- **Text Statistics**: Word count, character count, sentence count, readability scores
- **Sentiment Analysis**: Positive, negative, neutral sentiment detection with confidence scores
- **Social Media Elements**: Hashtag and mention extraction and counting
- **Content Insights**: Most common words and engagement optimization suggestions

### 📄 Document Processing
- **PDF Text Extraction**: Extract text from PDF documents while maintaining formatting
- **OCR for Images**: Extract text from image files (PNG, JPG, GIF, BMP, TIFF) using Tesseract OCR
- **Drag & Drop Interface**: User-friendly file upload with visual feedback
- **File Type Validation**: Automatic file type checking and error handling

### 💡 Engagement Suggestions
- Content length optimization recommendations
- Readability improvement tips
- Sentiment balance suggestions
- Hashtag usage optimization
- Call-to-action recommendations
- Question and emoji suggestions

## Technology Stack

### Backend
- **Flask**: Web framework for Python
- **PyPDF2**: PDF text extraction
- **Pytesseract**: OCR for image text extraction
- **NLTK**: Natural language processing and sentiment analysis
- **Textstat**: Readability score calculations
- **Pillow**: Image processing

### Frontend
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **Vanilla JavaScript**: Interactive functionality and API communication
- **Font Awesome**: Icons for enhanced UI

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Tesseract OCR installed on your system

#### Installing Tesseract:
- **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract`
- **Ubuntu/Debian**: `sudo apt install tesseract-ocr`

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd social-media-content-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

5. **Create templates directory**
   ```bash
   mkdir templates
   ```
   
6. **Move index.html to templates folder**
   ```bash
   mv index.html templates/
   ```

## Running the Application

### Development Mode
```bash
python app.py
```
The application will be available at `http://localhost:5000`

### Production Mode
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Project Structure
```
social-media-content-analyzer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML template
├── uploads/              # Temporary file storage (created automatically)
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created during setup)
```

## API Endpoints

### POST /upload
Upload and analyze document files (PDF or images)

**Request**: 
- Multipart form data with file field

**Response**:
```json
{
  "success": true,
  "filename": "document.pdf",
  "extracted_text": "extracted text content...",
  "analysis": {
    "statistics": {...},
    "sentiment": {...},
    "social_elements": {...},
    "common_words": [...],
    "suggestions": [...]
  }
}
```

### POST /analyze
Analyze text content directly

**Request**:
```json
{
  "text": "Your social media content here..."
}
```

**Response**:
```json
{
  "success": true,
  "analysis": {
    "statistics": {...},
    "sentiment": {...},
    "social_elements": {...},
    "common_words": [...],
    "suggestions": [...]
  }
}
```

## Features Breakdown

### Text Statistics
- Word count, character count, sentence count
- Flesch Reading Ease score (0-100, higher = easier to read)
- Flesch-Kincaid Grade Level (reading grade level required)

### Sentiment Analysis
- NLTK VADER sentiment analyzer
- Compound score (-1 to 1, negative to positive)
- Individual positive, neutral, negative scores
- Overall sentiment classification

### Social Media Elements
- Automatic hashtag detection (#hashtag)
- Mention detection (@username)
- Count and display of social elements

### Engagement Suggestions
- Content length optimization (20-100 words ideal)
- Readability improvements for broad audience reach
- Sentiment balance recommendations
- Hashtag usage optimization (3-5 recommended)
- Call-to-action suggestions
- Question prompts for engagement
- Emoji usage recommendations

## Error Handling
- File size limits (16MB maximum)
- File type validation
- OCR processing errors
- Text extraction failures
- Network error handling
- User-friendly error messages

## Browser Compatibility
- Chrome/Chromium 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Security Features
- File type validation
- Secure filename handling
- Temporary file cleanup
- Input sanitization
- CORS configuration

## Performance Optimization
- File size limits
- Efficient text processing
- Minimal dependencies
- Responsive design
- Loading states for better UX

## Future Enhancements
- Multi-language support
- Advanced ML-based suggestions
- Social media platform-specific optimization
- Batch file processing
- User accounts and history
- API rate limiting
- Advanced analytics dashboard

## Deployment
The application is ready for deployment on platforms like:
- Heroku
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk
- Google Cloud Run

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License
This project is licensed under the MIT License.

## Support
For issues and questions, please create an issue in the GitHub repository.
