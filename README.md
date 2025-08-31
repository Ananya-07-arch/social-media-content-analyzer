# Social Media Content Analyzer

🔗 **Live Demo**: [Coming Soon - Deploy on Railway/Heroku]  
📁 **GitHub Repository**: https:/Ananya-07-arch/github.com/e/social-media-content-analyzer

A web application that analyzes social media posts and suggests engagement improvements through document upload (PDF, images) or direct text input.

## 🎯 **Technical Assessment Project**
This project was developed as part of a Software Engineering technical assessment, demonstrating:
- Full-stack web development skills
- Document processing and OCR capabilities
- Natural language processing and sentiment analysis
- Modern UI/UX design
- Production-ready code architecture

## 🚀 **Quick Start**

```bash
# Clone the repository
git clone https://github.com/yourusername/social-media-content-analyzer.git
cd social-media-content-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` to use the application.

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
   git clone https://github.com/yourusername/social-media-content-analyzer.git
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

### POST /analyze
Analyze text content directly

## Screenshots

![Application Demo](screenshot.png) *Coming Soon*

## Future Enhancements
- Multi-language support
- Advanced ML-based suggestions
- Social media platform-specific optimization
- Batch file processing
- User accounts and history
- API rate limiting
- Advanced analytics dashboard

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License
This project is licensed under the MIT License.

## Contact
- **GitHub**: [Ananya-07-arch](https://github.com/yourusername)
- **Email**: ananyasrivastava0304@gmail.com
  

---

*This project demonstrates full-stack development capabilities including document processing, natural language processing, and modern web application architecture.*

