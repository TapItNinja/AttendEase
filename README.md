# FaceTrack Attendance System 📋

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/Face-recognition.jpg" alt="FaceTrack Logo" width="200"/>
  
  <h3>Smart Attendance Tracking with Face Recognition</h3>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.18+-red.svg)](https://streamlit.io/)
  [![Status](https://img.shields.io/badge/Status-Active-4CAF50.svg)](https://github.com/yourusername/facetrack-attendance)
</div>

## 🔍 Overview

FaceTrack is a modern attendance management system that uses facial recognition technology to automate attendance tracking. Perfect for classrooms, offices, and events, FaceTrack eliminates the need for traditional sign-in methods, offering a contactless, efficient, and secure way to record attendance.

## 📱 Application Showcase

<div align="center">
  <table>
    <tr>
      <td align="center">Face Registration</td>
      <td align="center">Attendance Tracking</td>
      <td align="center">Dashboard Analytics</td>
    </tr>
    <tr>
      <td><img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Face_detection.jpg" width="200"/></td>
      <td><img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Facial-recognition-system-concept.jpg" width="200"/></td>
      <td><img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/Dashboard_digital.jpg" width="200"/></td>
    </tr>
  </table>
</div>

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>👤 Face Registration</h3>
      <ul>
        <li>Quick and easy face enrollment process</li>
        <li>Captures multiple samples for higher accuracy</li>
        <li>User-friendly interface with real-time feedback</li>
        <li>Secure storage of facial data</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🔄 Real-time Recognition</h3>
      <ul>
        <li>Fast and accurate face detection</li>
        <li>Instant identification of registered users</li>
        <li>Automatic attendance marking</li>
        <li>Works in various lighting conditions</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>📊 Analytics Dashboard</h3>
      <ul>
        <li>Comprehensive attendance statistics</li>
        <li>Daily, weekly, and monthly reports</li>
        <li>Interactive data visualization</li>
        <li>Export options for further analysis</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🔒 Security & Privacy</h3>
      <ul>
        <li>Encrypted facial data storage</li>
        <li>No cloud dependencies, all data stored locally</li>
        <li>Customizable data retention policies</li>
        <li>GDPR-compliant implementation options</li>
      </ul>
    </td>
  </tr>
</table>

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Webcam or camera device
- 4GB RAM minimum (8GB recommended)
- 50MB free disk space for the application
- Additional space for attendance records

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/facetrack-attendance.git
   cd facetrack-attendance
   ```

2. Create and activate a virtual environment
   ```bash
   # For Linux/Mac
   python -m venv venv
   source venv/bin/activate
   
   # For Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the required directories and download resources
   ```bash
   # For Linux/Mac
   chmod +x setup.sh
   ./setup.sh
   
   # For Windows
   setup.bat
   ```

## 🛠️ Project Structure

```
facetrack-attendance/
│
├── data/                  # Data directory
│   └── haarcascade_frontalface_default.xml
│
├── Attendance/            # Attendance records directory
│
├── add_faces.py           # Face registration script
├── test.py                # Attendance system script
├── app.py                 # Streamlit dashboard
├── requirements.txt       # Package requirements
├── setup.sh               # Setup script for Linux/Mac
├── setup.bat              # Setup script for Windows
└── README.md              # This file
```

## 📋 Usage Guide

### Step 1: Register Faces

```bash
python add_faces.py
```
- Follow the on-screen prompts to enter your name
- Position your face in front of the camera
- The system will capture multiple samples of your face
- Registration completes automatically after sufficient samples

### Step 2: Run the Attendance System

```bash
python test.py
```
- The system will start your camera and begin recognizing faces
- When a registered face is detected, attendance is marked automatically
- The system displays the name of the recognized person
- Press 'q' to quit the application

### Step 3: View Attendance Dashboard

```bash
streamlit run app.py
```
- Open the provided URL in your web browser
- View today's attendance statistics
- Explore the attendance records
- Export data as needed

### Run Everything at Once

```bash
# For Linux/Mac
./run.sh

# For Windows
run.bat
```

## 🔧 Tech Stack

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

## 🌟 Key Highlights

- **Simple Setup**: Easy installation with minimal dependencies
- **Real-time Performance**: Fast face detection and recognition
- **Privacy-focused**: All data stored locally, no cloud dependencies
- **Customizable**: Easily adaptable for different environments
- **Interactive Dashboard**: Comprehensive attendance analytics
- **Export Options**: Support for CSV, Excel, and PDF exports

## 🔮 Future Roadmap

- [ ] Mobile app for remote attendance monitoring
- [ ] Multi-camera support for larger venues
- [ ] Integration with calendar systems for scheduling
- [ ] Anti-spoofing measures for enhanced security
- [ ] Attendance notifications and alerts
- [ ] Advanced analytics with machine learning insights

## 🛡️ Privacy Considerations

- Always obtain consent before registering faces
- Implement appropriate data retention policies
- Consider local privacy laws and regulations
- Provide clear information about data usage
- Allow users to request data deletion

## ⚠️ Limitations

- Performance may vary based on lighting conditions
- Requires fairly consistent facial appearance (affected by significant changes in appearance)
- Designed for controlled environments with cooperative users
- Not intended for covert surveillance applications

## 🔧 Troubleshooting

**Camera Not Detected**
```bash
# Check camera access
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened()); cap.release()"
```

**Face Not Detected**
- Ensure good lighting
- Position face directly in front of camera
- Try different angles during registration

**Import Errors**
```bash
# Verify package installation
pip list
# Reinstall requirements
pip install --no-cache-dir -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- OpenCV community for face detection algorithms
- Streamlit team for the amazing dashboard framework
- All contributors who have helped improve this project

---

<div align="center">
  <p>Made with ❤️ for smarter attendance tracking</p>
</div>
