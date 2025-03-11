import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re

load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

def calculate_resume_score(resume_text):
    score = 0
    word_count = len(resume_text.split())

    if 'experience' in resume_text.lower():
        score += 25
    if 'education' in resume_text.lower():
        score += 20
    if 'skills' in resume_text.lower():
        score += 20
    
    if word_count > 300:
        score += 10
    
  
    if len(re.findall(r'\•', resume_text)) > 3:  
        score += 10
    if len(re.findall(r'\d{4}', resume_text)) > 1:  
        score += 10

    return min(score, 100)

def provide_impressions(score):
    if score >= 90:
        return "Your resume is outstanding! It covers key elements effectively and presents your skills and experiences well."
    elif score >= 70:
        return "Your resume is strong, but there is room for improvement. Consider enhancing the clarity or adding more details about your accomplishments."
    elif score >= 50:
        return "Your resume is average. Adding more structured information about your skills, projects, or experiences could improve it significantly."
    else:
        return "Your resume needs improvement. Focus on adding key sections like skills, experiences, and education, and use clear formatting."

def suggest_internships(resume_text):
    skills = re.findall(r'\b(?:Python|Java|SQL|Machine Learning|Data Analysis|Project Management|Web Development|Cloud Computing|Cybersecurity)\b', resume_text, re.IGNORECASE)
    internships = []

    if 'python' in [skill.lower() for skill in skills]:
        internships.append("Python Developer Intern")
    if 'machine learning' in [skill.lower() for skill in skills]:
        internships.append("Machine Learning Intern")
    if 'data analysis' in [skill.lower() for skill in skills]:
        internships.append("Data Analyst Intern")
    if 'project management' in [skill.lower() for skill in skills]:
        internships.append("Project Management Intern")
    if 'web development' in [skill.lower() for skill in skills]:
        internships.append("Web Development Intern")
    if 'cloud computing' in [skill.lower() for skill in skills]:
        internships.append("Cloud Computing Intern")
    if 'cybersecurity' in [skill.lower() for skill in skills]:
        internships.append("Cybersecurity Intern")

    if not internships:
        internships.append("General Internship in Technology or Business")

    return internships

def suggest_jobs(resume_text):
    skills_projects = re.findall(r'\b(?:Python|Java|SQL|Machine Learning|Data Analysis|Web Development|Cloud Computing|Cybersecurity|DevOps|AI|NLP|Big Data|Project Management)\b', resume_text, re.IGNORECASE)
    job_roles = []

    if 'python' in [item.lower() for item in skills_projects]:
        job_roles.append("Python Developer")
    if 'machine learning' in [item.lower() for item in skills_projects]:
        job_roles.append("Machine Learning Engineer")
    if 'data analysis' in [item.lower() for item in skills_projects]:
        job_roles.append("Data Analyst")
    if 'web development' in [item.lower() for item in skills_projects]:
        job_roles.append("Frontend Developer")
        job_roles.append("Full Stack Developer")
    if 'cloud computing' in [item.lower() for item in skills_projects]:
        job_roles.append("Cloud Engineer")
    if 'cybersecurity' in [item.lower() for item in skills_projects]:
        job_roles.append("Cybersecurity Analyst")
    if 'devops' in [item.lower() for item in skills_projects]:
        job_roles.append("DevOps Engineer")
    if 'ai' in [item.lower() for item in skills_projects] or 'nlp' in [item.lower() for item in skills_projects]:
        job_roles.append("AI Researcher")
        job_roles.append("NLP Engineer")
    if 'big data' in [item.lower() for item in skills_projects]:
        job_roles.append("Big Data Engineer")
    if 'project management' in [item.lower() for item in skills_projects]:
        job_roles.append("Project Manager")

    if not job_roles:
        job_roles.append("Entry-Level Positions in Relevant Fields")

    return job_roles

chatbot_prompt = """
You are a highly experienced Application Tracking System (ATS) with a deep understanding of the tech field, software engineering, data science, and big data engineering. You are reviewing the following resume and assisting with various queries:

Resume: {text}

User's Query: {query}

Please provide a standalone answer specific to this query.
"""

st.title("Smart ATS Chatbot")
st.text("Ask questions about your resume!")

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF of your resume.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file is not None:
    text = input_pdf_text(uploaded_file) 
    st.session_state.resume_text = text  

    resume_score = calculate_resume_score(text)
    st.subheader("Resume Preparation Score")
    st.write(f"Your Resume Preparation Score is: **{resume_score}%**")

    impressions = provide_impressions(resume_score)
    st.subheader("Impressions of Your Resume")
    st.write(impressions)

    internships = suggest_internships(text)
    st.subheader("Suggested Internships")
    st.write("Here are some internships you might consider:")
    for internship in internships:
        st.write(f"- {internship}")

    job_roles = suggest_jobs(text)
    st.subheader("Suggested Job Roles")
    st.write("Based on your resume, here are some job roles you might explore:")
    for job in job_roles:
        st.write(f"- {job}")

    st.subheader("Chat with the ATS")
    user_query = st.text_input("Ask your question about your resume:")

    if user_query:
        formatted_prompt = chatbot_prompt.format(text=text, query=user_query)
        
        response = get_gemini_response(formatted_prompt)

        st.session_state.chat_history.append({"role": "ats", "query": user_query, "response": response})

        st.write(f"**You:** {user_query}")
        st.write(f"**ATS:** {response}")

else:
    st.warning("Please upload a valid PDF file.")
