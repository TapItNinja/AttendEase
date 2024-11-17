# facerecog


Here's a complete setup guide to make the attendance system work anywhere:

1. **System Requirements**:
   - Python 3.8 or higher
   - Webcam (for face detection)
   - Sufficient storage for face data and attendance records

2. **Project Structure**:
```plaintext
attendance_system/
│
├── data/
│   └── haarcascade_frontalface_default.xml
├── Attendance/
├── add_faces.py
├── test.py
├── app.py
└── requirements.txt
```

3. **Installation Steps**:

```bash
# 1. Create a new virtual environment
python -m venv venv

# 2. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Download the face detection cascade file
# Create a 'data' directory and download haarcascade_frontalface_default.xml from:
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
```

4. **Usage Instructions**:

```bash
# 1. First, register faces:
python add_faces.py

# 2. Run the attendance system:
python test.py

# 3. Start the dashboard:
streamlit run app.py
```

5. **Additional Setup Notes**:

- Ensure proper lighting for face detection
- Each person should be registered with at least 100 face samples
- The webcam should have a clear, unobstructed view
- Consider using a background image for better visualization

6. **Troubleshooting Common Issues**:

```python
# If OpenCV camera doesn't work, try changing the camera index:
# In test.py and add_faces.py, modify:
self.video = cv2.VideoCapture(0)  # Try 1 or 2 if 0 doesn't work

# If face detection is poor, adjust detection parameters:
faces = self.facedetect.detectMultiScale(gray, 1.3, 5)  # Adjust 1.3 and 5

# If the Streamlit dashboard doesn't show data:
# Check the Attendance directory for CSV files
# Verify CSV format has correct headers: NAME,TIME
```

7. **Optional Environment Variables**:
```bash
# Create a .env file with these settings (optional):
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
```

8. **Running on Different Operating Systems**:

Windows:
```batch
# Create batch file (start_system.bat):
@echo off
call venv\Scripts\activate
start python test.py
timeout 2
start streamlit run app.py
```

macOS/Linux:
```bash
# Create shell script (start_system.sh):
#!/bin/bash
source venv/bin/activate
python test.py &
sleep 2
streamlit run app.py
```

9. **Backup and Maintenance**:

```bash
# Create backup script (backup.py):
import shutil
from datetime import datetime

backup_date = datetime.now().strftime("%Y%m%d")
shutil.make_archive(f'backup_{backup_date}', 'zip', 'Attendance')
```

10. **Security Considerations**:

- Keep the `data` directory secure as it contains facial data
- Regularly backup the attendance records
- Consider implementing user authentication for the dashboard
- Use HTTPS if deploying the dashboard publicly

Follow these instructions carefully and the system should work on any compatible system. If you encounter any issues, try these troubleshooting steps:

1. Check if all dependencies are installed:
```bash
pip list
```

2. Verify Python version:
```bash
python --version
```

3. Test camera access:
```python
import cv2
cap = cv2.VideoCapture(0)
print(cap.isOpened())
```

4. Check file permissions:
```python
import os
print(os.access("Attendance", os.W_OK))
print(os.access("data", os.R_OK))
```



