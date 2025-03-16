# AttendEase 📋

<div align="center">
  <img src="https://github.com/TapItNinja/AttendEase/raw/main/Components/Face-recognition.jpeg" alt="AttendEase Logo" width="200"/>
  
  <h3>Advanced Facial Recognition Attendance System</h3>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.18+-red.svg)](https://streamlit.io/)
  [![Status](https://img.shields.io/badge/Status-Completed-4CAF50.svg)](https://github.com/TapItNinja/AttendEase)
  [![Year](https://img.shields.io/badge/Year_Project-7th-purple.svg)](https://github.com/TapItNinja/AttendEase)
</div>

## 🎓 7th Semester Academic Project

AttendEase is an innovative facial recognition attendance system developed as a final year academic project. This system reimagines traditional attendance tracking in educational institutions by leveraging computer vision and machine learning technologies to create an automated, contactless solution.

## 📱 Application Showcase

<div align="center">
  <table>
    <tr>
      <td align="center">Face Registration</td>
      <td align="center">Recognition Process</td>
      <td align="center">Interactive Dashboard</td>
    </tr>
    <tr>
      <td><img src="https://github.com/TapItNinja/AttendEase/raw/main/Components/Face_detection.png" width="280"/></td>
      <td><img src="https://github.com/TapItNinja/AttendEase/raw/main/Components/Facial-recognition-system-concept.png" width="280"/></td>
      <td><img src="https://github.com/TapItNinja/AttendEase/raw/main/Components/Dashboard_digital.png" width="280"/></td>
    </tr>
  </table>
</div>

## ✨ Core Features

<table>
  <tr>
    <td width="50%">
      <h3>👤 Intelligent Face Registration</h3>
      <ul>
        <li>Multi-sample face capture for greater accuracy</li>
        <li>Real-time visual feedback during registration</li>
        <li>Automatic facial data processing and storage</li>
        <li>User-friendly registration interface</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🔄 Seamless Recognition Engine</h3>
      <ul>
        <li>Real-time face detection and recognition</li>
        <li>Advanced Haar Cascade classification</li>
        <li>Optimized for classroom/lab environments</li>
        <li>Performance tuned for multiple faces in frame</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>📊 Comprehensive Analytics</h3>
      <ul>
        <li>Interactive Streamlit dashboard with real-time updates</li>
        <li>Class attendance percentage visualization</li>
        <li>Individual student attendance records</li>
        <li>Exportable reports for academic records</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🔒 Privacy-First Design</h3>
      <ul>
        <li>Locally stored facial data with no cloud dependencies</li>
        <li>Pickle-based secure data serialization</li>
        <li>Consent-based registration process</li>
        <li>Data management tools for administrators</li>
      </ul>
    </td>
  </tr>
</table>

## 🚀 Getting Started

### System Requirements

- Python 3.8 or higher
- Webcam (720p recommended for optimal performance)
- 4GB RAM (8GB recommended)
- Windows 10/11, macOS, or Linux

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/TapItNinja/AttendEase.git
   cd AttendEase
   ```

2. Set up a virtual environment
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate
   
   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required packages
   ```bash
   pip install -r requirements.txt
   ```

4. Run the setup script
   ```bash
   # For Windows
   setup.bat
   
   # For macOS/Linux
   chmod +x setup.sh
   ./setup.sh
   ```

## 📋 How to Use

### Step 1: Register Student Faces

```bash
python add_faces.py
```

- Enter student name when prompted
- Position face in the frame (indicated by green box)
- System captures 100 samples automatically
- Registration completes with confirmation message

### Step 2: Mark Attendance with Face Recognition

```bash
python test.py
```

- Camera activates and begins scanning for faces
- Recognized students are marked present automatically
- Attendance saved to CSV file with timestamp
- Press 'q' to exit the recognition system

### Step 3: View Attendance Dashboard

```bash
streamlit run app.py
```

- Opens interactive dashboard in your default browser
- Displays today's attendance statistics
- Shows individual attendance records
- Provides export options for reporting

### All-in-One Launch Script

```bash
# For Windows
run.bat

# For macOS/Linux
./run.sh
```

## 📁 Project Structure

```
AttendEase/
│
├── Components/             # Project images and assets
│
├── data/                   # Face detection models
│   └── haarcascade_frontalface_default.xml
│
├── Attendance/             # Daily attendance records (CSV)
│
├── add_faces.py            # Face registration module
├── test.py                 # Attendance tracking system
├── app.py                  # Streamlit dashboard
│
├── requirements.txt        # Package dependencies
├── setup.sh                # Setup script for Unix systems
├── setup.bat               # Setup script for Windows
├── run.sh                  # Run script for Unix systems
├── run.bat                 # Run script for Windows
└── README.md               # Project documentation
```

## 🛠️ Technology Stack

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="40"/><br/>Python</td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" width="40"/><br/>OpenCV</td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" width="40"/><br/>Streamlit</td>
    </tr>
    <tr>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="40"/><br/>Pandas</td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width="40"/><br/>NumPy</td>
      <td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="40"/><br/>Scikit-learn</td>
    </tr>
  </table>
</div>

## 🌟 Project Highlights

- **Academic Innovation**: Developed as a comprehensive 7th year project
- **Efficient Processing**: Optimized algorithms for real-time recognition
- **User-Centered Design**: Intuitive interfaces for students and instructors
- **Data Visualization**: Interactive dashboard for attendance analytics
- **Deployment Ready**: Fully functional system for immediate use

## 🔍 Technical Implementation

### Face Detection & Recognition Process

1. **Preprocessing**:
   - Image conversion to grayscale
   - Haar Cascade Classifier for face detection
   - Face region extraction

2. **Feature Extraction**:
   - Facial data normalization
   - Image resizing (50×50 pixels)
   - Data flattening for processing

3. **Recognition Algorithm**:
   - K-Nearest Neighbors (KNN) classification
   - Confidence score calculation
   - Threshold-based verification

4. **Data Management**:
   - Pickle serialization for model storage
   - CSV-based attendance records
   - Pandas DataFrame processing

## 🔮 Future Enhancements

- [ ] Multi-camera support for larger classrooms
- [ ] Mobile application for administrative monitoring
- [ ] Enhanced anti-spoofing measures
- [ ] Integration with academic management systems
- [ ] Cloud synchronization options for backup
- [ ] Real-time attendance notifications

## 🛟 Troubleshooting Guide

**Camera Not Detected**
```bash
# Verify camera availability
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera OK' if cap.isOpened() else 'Camera Failed'); cap.release()"
```

**Face Not Detected**
- Ensure adequate lighting (avoid backlighting)
- Position face directly in frame
- Check if haarcascade file is correctly downloaded

**Dashboard Not Loading**
```bash
# Check Streamlit installation
streamlit --version
# Reinstall if needed
pip install --force-reinstall streamlit
```

## 👥 Development Team

- **Project Lead**: [TapItNinja](https://github.com/TapItNinja)
- **Computer Vision Specialist**: [Your Name]
- **Frontend Developer**: [Team Member]
- **Testing & Documentation**: [Team Member]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Academic advisors for project guidance
- OpenCV community for computer vision resources
- Streamlit developers for the dashboard framework
- Fellow students for testing and feedback

---

<div align="center">
  <p>Developed as a 7th Year Academic Project with ❤️ by Team AttendEase</p>
  <a href="https://github.com/TapItNinja">
    <img src="https://img.shields.io/badge/GitHub-TapItNinja-black?style=social&logo=github" alt="GitHub Profile"/>
  </a>
</div>
