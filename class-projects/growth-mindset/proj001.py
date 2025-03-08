import streamlit as st

# Set page configuration
st.set_page_config(page_title="E-Learning", page_icon="📚", layout="wide")

# Title of the app
st.title("E-Learning: Tech Education Platform")

# Sidebar for navigation
st.sidebar.title("E-Learning Menu")
options = ["File Upload Center", "Learning Center", "Progress Tracker", "Community Forum", "Settings"]
choice = st.sidebar.radio("Explore the Menu", options)

# File Upload Center Section
if choice == "File Upload Center":
    st.header("File Upload Center")
    st.write("Upload your project files")
    
    uploaded_file = st.file_uploader("Drag and drop file here", type=["py", "txt", "pdf", "jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.success("File Uploaded Successfully")
        st.write("File Details:")
        st.write(f"Name: {uploaded_file.name}")
        st.write(f"Type: {uploaded_file.type}")
        st.write(f"Size: {uploaded_file.size/1024} kb")
    
    st.write("**Limit 20MB per file • PY, TXT, PDF, JPG, PNG, JPEG**")
    st.write("---")
    st.write("Experience is the name everyone gives to their mistakes. - Oscar Wilde")

# Learning Center Section
elif choice == "Learning Center":
    st.header("Learning Center")
    
    # User Information
    st.subheader("Your Name")
    name = st.text_input("Enter your name")
    
    st.subheader("Learning Goal")
    learning_goal = st.text_input("Enter your learning goal")
    
    st.subheader("Choose Your Path")
    path = st.selectbox("Select your path", ["Cybersecurity", "Web Development", "Data Science", "Machine Learning"])
    
    st.subheader("Experience Level")
    experience_level = st.radio("Select your experience level", ["Beginner", "Intermediate", "Expert"])
    
    st.subheader("Preferred Programming Languages")
    languages = st.multiselect("Select your preferred programming languages", ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"])
    
    st.subheader("Daily Study Hours")
    study_hours = st.slider("Select your daily study hours", 0, 12)
    
    if st.button("Submit Learning Preferences"):
        st.success("Learning Preferences Submitted")
        st.write(f"Name: {name}")
        st.write(f"Learning Goal: {learning_goal}")
        st.write(f"Path: {path}")
        st.write(f"Experience Level: {experience_level}")
        st.write(f"Preferred Languages: {', '.join(languages)}")
        st.write(f"Daily Study Hours: {study_hours} hours")

# Progress Tracker Section
elif choice == "Progress Tracker":
    st.header("Progress Tracker")
    
    st.subheader("Course Progress")
    course = st.selectbox("Select Course", ["Introduction to Python", "Advanced Python", "Data Science", "Machine Learning"])
    progress = st.slider("Progress", 0, 100)
    st.write(f"You have completed {progress}% of {course}")
    
    st.subheader("Quiz Scores")
    quiz = st.selectbox("Select Quiz", ["Quiz 1", "Quiz 2", "Quiz 3"])
    score = st.number_input("Enter your score", min_value=0, max_value=100)
    st.write(f"Your score for {quiz} is {score}%")
    
    if st.button("Update Progress"):
        st.success("Progress Updated Successfully")

# Community Forum Section
elif choice == "Community Forum":
    st.header("Community Forum")
    
    st.subheader("Recent Discussions")
    discussions = ["Best resources for Python?", "How to start with Machine Learning?", "Tips for Cybersecurity beginners"]
    selected_discussion = st.selectbox("Select a discussion", discussions)
    st.write(f"Selected Discussion: {selected_discussion}")
    
    st.subheader("Post a Question")
    question = st.text_area("Enter your question")
    if st.button("Post Question"):
        st.success("Question Posted Successfully")
        st.write(f"Posted Question: {question}")

# Settings Section
elif choice == "Settings":
    st.header("Settings")
    
    st.subheader("Account Settings")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    st.subheader("Notification Preferences")
    email_notifications = st.checkbox("Enable Email Notifications")
    push_notifications = st.checkbox("Enable Push Notifications")
    
    if st.button("Save Settings"):
        st.success("Settings Saved Successfully")
        st.write(f"Username: {username}")
        st.write(f"Email: {email}")
        st.write(f"Email Notifications: {'Enabled' if email_notifications else 'Disabled'}")
        st.write(f"Push Notifications: {'Enabled' if push_notifications else 'Disabled'}")