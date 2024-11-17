from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from pathlib import Path

class AttendanceSystem:
    def __init__(self):
        self.setup_directories()
        self.load_models()
        self.initialize_camera()
        self.setup_background()
        
    def setup_directories(self):
        """Create necessary directories"""
        Path("data").mkdir(exist_ok=True)
        Path("Attendance").mkdir(exist_ok=True)
    
    def load_models(self):
        """Load the trained model and face detection cascade"""
        try:
            with open('data/names.pkl', 'rb') as w:
                self.LABELS = pickle.load(w)
            with open('data/faces_data.pkl', 'rb') as f:
                self.FACES = pickle.load(f)
                
            self.facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
            
            self.knn = KNeighborsClassifier(n_neighbors=5)
            self.knn.fit(self.FACES, self.LABELS)
            
        except FileNotFoundError as e:
            raise Exception("Required model files not found. Please run add_faces.py first.")
    
    def initialize_camera(self):
        """Initialize video capture"""
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            raise Exception("Could not open video capture device")
    
    def setup_background(self):
        """Load background image"""
        if os.path.exists("background.png"):
            self.imgBackground = cv2.imread("background.png")
        else:
            self.imgBackground = np.zeros((800, 750, 3), dtype=np.uint8)
    
    def notify_attendance(self, message):
        """Print attendance notification"""
        print(f"\n>>> {message} <<<\n")
    
    def save_attendance(self, name, timestamp):
        """Save attendance record to CSV"""
        date = datetime.now().strftime("%d-%m-%Y")
        attendance_file = f"Attendance/Attendance_{date}.csv"
        
        is_new_file = not os.path.exists(attendance_file)
        
        with open(attendance_file, "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            if is_new_file:
                writer.writerow(['NAME', 'TIME'])
            writer.writerow([name, timestamp])
    
    def run(self):
        """Main loop for face recognition and attendance"""
        try:
            print("\nAttendance System Running...")
            print("Press 'o' to mark attendance")
            print("Press 'q' to quit\n")
            
            while True:
                ret, frame = self.video.read()
                if not ret:
                    break
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.facedetect.detectMultiScale(gray, 1.3, 5)
                
                for (x, y, w, h) in faces:
                    # Process face and get prediction
                    crop_img = frame[y:y+h, x:x+w, :]
                    resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
                    output = self.knn.predict(resized_img)
                    
                    # Draw face detection visualization
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
                    cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
                    cv2.putText(frame, str(output[0]), (x, y-15), 
                              cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                
                # Update display
                if self.imgBackground.shape[0] >= 162 + frame.shape[0] and \
                   self.imgBackground.shape[1] >= 55 + frame.shape[1]:
                    self.imgBackground[162:162 + frame.shape[0], 
                                    55:55 + frame.shape[1]] = frame
                    cv2.imshow("Attendance System", self.imgBackground)
                else:
                    cv2.imshow("Attendance System", frame)
                
                key = cv2.waitKey(1)
                
                if key == ord('o'):  # Mark attendance
                    if len(faces) > 0:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        self.save_attendance(str(output[0]), timestamp)
                        self.notify_attendance("Attendance Marked Successfully!")
                        time.sleep(1)
                    else:
                        self.notify_attendance("No face detected!")
                
                elif key == ord('q'):  # Quit
                    break
                    
        except Exception as e:
            print(f"Error in main loop: {str(e)}")
        finally:
            self.video.release()
            cv2.destroyAllWindows()

def main():
    try:
        system = AttendanceSystem()
        system.run()
    except Exception as e:
        print(f"System Error: {str(e)}")

if __name__ == "__main__":
    main()