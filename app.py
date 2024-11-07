import streamlit as st
import pandas as pd
from datetime import time

# Title
st.title("Student Daily Timetable")

# Introduction
st.write("Create your day timetable by adding tasks with times and descriptions.")

# Initialize session state to store timetable data
if 'timetable' not in st.session_state:
    st.session_state['timetable'] = []

# Input form for adding a task
with st.form("task_form"):
    task_name = st.text_input("Task Name", placeholder="Enter the task (e.g., Math Study, Gym, Lunch)")
    start_time = st.time_input("Start Time", value=time(9, 0))
    end_time = st.time_input("End Time", value=time(10, 0))
    task_description = st.text_area("Description", placeholder="Brief description of the task")
    submit_button = st.form_submit_button("Add Task")

# Add task to timetable
if submit_button:
    if start_time < end_time:
        st.session_state['timetable'].append({
            "Task": task_name,
            "Start Time": start_time.strftime("%H:%M"),
            "End Time": end_time.strftime("%H:%M"),
            "Description": task_description
        })
        st.success(f"Added task: {task_name}")
    else:
        st.error("End time should be after start time.")

# Display timetable
if st.session_state['timetable']:
    st.write("### Your Timetable")
    timetable_df = pd.DataFrame(st.session_state['timetable'])
    st.table(timetable_df)
else:
    st.write("No tasks added yet. Please add tasks to build your timetable.")

# Clear all tasks
if st.button("Clear Timetable"):
    st.session_state['timetable'] = []
    st.write("Timetable cleared.")
