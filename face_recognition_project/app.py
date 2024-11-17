import streamlit as st
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

def setup_page():
    try:
        st.set_page_config(
            page_title="Attendance Dashboard",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    except:
        pass  # Page config already set
    st.title("Attendance Dashboard 📊")

@st.cache_data(ttl=300)  # Cache data for 5 minutes
def load_attendance_data():
    """Load attendance data with caching"""
    try:
        date = datetime.now().strftime("%d-%m-%Y")
        file_path = f"Attendance/Attendance_{date}.csv"
        
        if not os.path.exists(file_path):
            return None
            
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    # Basic setup
    setup_page()
    
    # Ensure directory exists
    Path("Attendance").mkdir(exist_ok=True)
    
    try:
        # Load data
        df = load_attendance_data()
        
        if df is None:
            st.warning("No attendance records found for today.")
            st.stop()
            
        # Display basic stats
        st.subheader("Today's Attendance")
        total_attendees = len(df['NAME'].unique()) if df is not None else 0
        st.metric("Total Attendees", total_attendees)
        
        # Display attendance table
        if df is not None and not df.empty:
            st.subheader("Attendance Records")
            st.dataframe(df, use_container_width=True)
            
            # Export option
            if st.button("Export to CSV"):
                date = datetime.now().strftime("%d-%m-%Y")
                df.to_csv(f"Attendance/Attendance_Export_{date}.csv", index=False)
                st.success("Export successful!")
                
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()

if __name__ == "__main__":
    main()