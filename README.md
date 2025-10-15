# 🎭 PlotTwist - AI-Assisted Thriller Story Generator

PlotTwist is a Python web application that generates spine-chilling thriller stories using AI-powered text generation. Built with Flask and Markov chains, it creates unique plot twists and engaging narratives with every generation.

## Features

- 🤖 AI-powered story generation using Markov chains
- 📝 Customizable story parameters (length, starting words)
- 🎲 Random plot twist generation
- 💾 Save and manage your stories
- ✏️ Edit existing stories
- 🎨 Modern, responsive UI
- 🚀 Easy deployment to Heroku or Render

## Project Structure

```
cmps-357-fa25-plot-twist-ai-generator/
├── app/
│   ├── __init__.py           # App package initialization
│   └── story_generator.py    # Markov chain story generator
├── templates/
│   ├── index.html            # Home page with story generator
│   ├── stories.html          # List of saved stories
│   ├── story.html            # Individual story view
│   └── edit.html             # Story editing interface
├── static/
│   └── css/
│       └── style.css         # Application styles
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── LICENSE                  # MIT License
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/School-of-Computing-and-Informatics/cmps-357-fa25-plot-twist-ai-generator.git
   cd cmps-357-fa25-plot-twist-ai-generator
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Generate your first thriller story!**

## Usage

### Generating a Story

1. Visit the home page
2. (Optional) Enter starting words to guide the story
3. Set the number of sentences (3-30)
4. Choose whether to include a plot twist
5. Click "Generate Story"
6. Save or regenerate as desired

### Managing Stories

- View all saved stories at `/stories`
- Click on any story to read the full text
- Edit stories to customize them further
- Delete stories you no longer want

## Technology Stack

- **Backend:** Flask 3.0.0
- **Text Generation:** Markovify 0.9.4 (Markov chains)
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Ready for Heroku or Render

## 6-Week Development Milestone Plan

### Week 1: Project Setup & Foundation
- [x] Initialize Git repository
- [x] Create project structure (folders, files)
- [x] Set up Python virtual environment
- [x] Install Flask and dependencies
- [x] Create basic Flask app skeleton
- [x] Write comprehensive README

### Week 2: Core Story Generation
- [x] Implement Markov chain text generator
- [x] Create thriller story corpus
- [x] Build story generation API endpoint
- [x] Add plot twist generation
- [x] Test story generation with various parameters
- [x] Refine text generation quality

### Week 3: Web Interface Development
- [x] Design UI/UX wireframes
- [x] Create HTML templates (index, stories, story, edit)
- [x] Implement CSS styling with thriller theme
- [x] Add responsive design for mobile
- [x] Integrate frontend with backend APIs
- [x] Add loading states and animations

### Week 4: Story Management Features
- [x] Implement story saving functionality
- [x] Create story listing page
- [x] Add story viewing page
- [x] Implement story editing
- [x] Add story deletion
- [x] Test all CRUD operations

### Week 5: Polish & Enhancement
- [ ] Add database integration (SQLite/PostgreSQL)
- [ ] Implement user sessions
- [ ] Add story export functionality (PDF, text)
- [ ] Enhance error handling
- [ ] Add input validation
- [ ] Improve story generation algorithm
- [ ] Add unit tests
- [ ] Perform security audit

### Week 6: Deployment & Documentation
- [ ] Create deployment configuration (Heroku/Render)
- [ ] Set up production environment variables
- [ ] Configure production database
- [ ] Deploy to Heroku or Render
- [ ] Test deployed application
- [ ] Create user documentation
- [ ] Write deployment guide
- [ ] Prepare final presentation

## Future Enhancements

- 🔐 User authentication and accounts
- 🗄️ Database integration for persistent storage
- 🤖 Integration with GPT API for enhanced generation
- 📤 Export stories as PDF or ePub
- 🎨 Multiple genre support (horror, mystery, noir)
- 🌐 Story sharing and collaboration
- 📊 Story analytics and statistics
- 🎯 Advanced customization options

## Deployment

### Heroku Deployment

1. **Create a `Procfile`:**
   ```
   web: python app.py
   ```

2. **Create a `runtime.txt`:**
   ```
   python-3.11.0
   ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

### Render Deployment

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Deploy!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built as part of CMPS 357 - Fall 2025
- Powered by Markovify for text generation
- Inspired by classic thriller and mystery novels

## Contact

School of Computing and Informatics
- GitHub: [@School-of-Computing-and-Informatics](https://github.com/School-of-Computing-and-Informatics)

---

**Happy Story Generating! 📚✨**