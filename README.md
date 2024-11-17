
Here's a step-by-step guide with complete project structure:

1. **Create Project Directory**:
```plaintext
mkdir attendance_system
cd attendance_system
```

2. **Project Structure**:
```plaintext
attendance_system/
│
├── venv/                  # Virtual environment directory
│
├── data/                  # Data directory
│   └── haarcascade_frontalface_default.xml
│
├── Attendance/            # Attendance records directory
│
├── add_faces.py          # Face registration script
├── test.py               # Attendance system script
├── app.py                # Streamlit dashboard
└── requirements.txt      # Package requirements
```

3. **Complete Setup Script** (create as `setup.sh` for Linux/Mac or `setup.bat` for Windows):

For Linux/Mac (`setup.sh`):
```bash
#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create necessary directories
mkdir -p data
mkdir -p Attendance

# Download face cascade file
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml -P data/

# Make scripts executable
chmod +x add_faces.py
chmod +x test.py
chmod +x app.py

echo "Setup complete!"
```

For Windows (`setup.bat`):
```batch
@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Create necessary directories
mkdir data
mkdir Attendance

REM Download face cascade file (requires curl)
curl https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml -o data/haarcascade_frontalface_default.xml

echo Setup complete!
```

4. **Run Script** (create as `run.sh` for Linux/Mac or `run.bat` for Windows):

For Linux/Mac (`run.sh`):
```bash
#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the attendance system
python test.py &

# Wait a moment for the attendance system to start
sleep 2

# Run the Streamlit dashboard
streamlit run app.py

# The script will keep running until you close it
# When you're done, you can deactivate the virtual environment:
# deactivate
```

For Windows (`run.bat`):
```batch
@echo off

REM Activate virtual environment
call venv\Scripts\activate

REM Run the attendance system
start python test.py

REM Wait a moment for the attendance system to start
timeout /t 2

REM Run the Streamlit dashboard
streamlit run app.py

REM The script will keep running until you close it
REM When you're done, you can deactivate the virtual environment:
REM deactivate
```

5. **Verification Steps**:
```bash
# Check Python version in virtual environment
python --version

# Check installed packages
pip list

# Verify OpenCV installation
python -c "import cv2; print(cv2.__version__)"

# Check if camera is accessible
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened()); cap.release()"
```

6. **Troubleshooting Virtual Environment Issues**:
```bash
# If virtual environment isn't working:
rm -rf venv  # (Linux/Mac)
rmdir /s /q venv  # (Windows)

# Create new virtual environment
python -m venv venv

# If pip needs upgrading in virtual environment:
python -m pip install --upgrade pip

# If packages fail to install:
pip install --no-cache-dir -r requirements.txt
```

Remember to always activate the virtual environment before running any scripts:
```bash
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

And deactivate when you're done:
```bash
deactivate
```

This setup ensures that your application runs in an isolated environment with the correct package versions, preventing conflicts with other Python projects on your system.
