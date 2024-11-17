import cv2
import pickle
import numpy as np
import os
from pathlib import Path

def create_data_directory():
    """Create data directory if it doesn't exist"""
    Path("data").mkdir(exist_ok=True)
    Path("Attendance").mkdir(exist_ok=True)

def initialize_camera():
    """Initialize camera and face detection"""
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        raise Exception("Could not open video capture device")
    
    cascade_path = 'data/haarcascade_frontalface_default.xml'
    if not os.path.exists(cascade_path):
        raise FileNotFoundError(f"Cascade file not found at {cascade_path}")
    
    return video, cv2.CascadeClassifier(cascade_path)

def capture_faces(video, facedetect, name, required_samples=100):
    """Capture and process facial data"""
    faces_data = []
    i = 0
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w, :]
            resized_img = cv2.resize(crop_img, (50, 50))
            
            if len(faces_data) < required_samples and i % 10 == 0:
                faces_data.append(resized_img)
            i += 1
            
            # Draw face detection visualization
            cv2.putText(frame, f"Captures: {len(faces_data)}/{required_samples}", (30, 30), 
                       cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("Face Registration", frame)
        
        if cv2.waitKey(1) == ord('q') or len(faces_data) >= required_samples:
            break
    
    return np.array(faces_data)

def save_data(faces_data, name):
    """Save captured face data and names"""
    if len(faces_data) == 0:
        raise ValueError("No faces were captured")
    
    # Ensure we have exactly the required number of samples
    required_samples = 100
    if len(faces_data) < required_samples:
        raise ValueError(f"Not enough face samples. Got {len(faces_data)}, need {required_samples}")
    
    faces_data = faces_data[:required_samples]  # Ensure exact number of samples
    faces_data = faces_data.reshape(required_samples, -1)  # Flatten the images
    
    # Save or update names
    names_path = 'data/names.pkl'
    if os.path.exists(names_path):
        with open(names_path, 'rb') as f:
            names = pickle.load(f)
        names = list(names)  # Convert to list if it's not already
        names.extend([name] * required_samples)
    else:
        names = [name] * required_samples
    
    with open(names_path, 'wb') as f:
        pickle.dump(names, f)
    
    # Save or update face data
    faces_path = 'data/faces_data.pkl'
    if os.path.exists(faces_path):
        with open(faces_path, 'rb') as f:
            existing_faces = pickle.load(f)
        faces_data = np.vstack((existing_faces, faces_data))
    
    with open(faces_path, 'wb') as f:
        pickle.dump(faces_data, f)

def main():
    try:
        create_data_directory()
        video, facedetect = initialize_camera()
        
        # Get user name
        while True:
            name = input("Enter Your Name: ").strip()
            if name:
                break
            print("Name cannot be empty. Please try again.")
        
        print("\nStarting face capture...")
        print("Position your face in front of the camera")
        print("Press 'q' to quit if needed\n")
        
        # Capture faces
        faces_data = capture_faces(video, facedetect, name)
        
        if len(faces_data) < 100:
            print(f"\nNot enough face data captured ({len(faces_data)}/100).")
            print("Please try again with better lighting and face positioning.")
            return
            
        # Save the data
        save_data(faces_data, name)
        print(f"\nSuccessfully registered {name}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        video.release()
        cv2.destroyAllWindows()
        
    # Print data status
    try:
        with open('data/names.pkl', 'rb') as f:
            names = pickle.load(f)
        with open('data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
        print(f"\nTotal registered faces: {len(faces)//100}")
        print(f"Unique names: {len(set(names))}")
    except Exception as e:
        print("\nCould not read registration status")

if __name__ == "__main__":
    main()