
## Smart ATS Chatbot

**Overview:**

The Smart ATS Chatbot is a user-friendly application designed to analyze resumes, provide valuable feedback, and suggest suitable job opportunities. Utilizing advanced technologies like Google Gemini for natural language processing and PyPDF2 for text extraction, it offers an interactive experience for resume refinement and career exploration.

**Features:**

* **Resume Upload:** Easily upload your resume in PDF format for analysis.
* **Resume Preparation Score:** Receive a score based on key elements like experience, education, skills, and formatting to gauge your resume's effectiveness.
* **Personalized Feedback:** Get insights on how to improve your resume based on the generated score.
* **Internship Suggestions:** Discover relevant internship opportunities aligned with your skills and experience.
* **Job Role Recommendations:** Explore potential job roles based on the content of your resume.
* **Chat with ATS:** Interact with an AI-powered chatbot that answers questions regarding your resume and career path.

**Technologies Used:**

* **Streamlit:** Enables the creation of the interactive web application.
* **Google Gemini API:** Provides AI-powered responses and analyzes user queries.
* **PyPDF2:** Extracts text from uploaded PDF resumes.
* **dotenv:** Manages sensitive environment variables such as API keys securely.
* **Regex:** Analyzes resume content to extract skills, experience, and dates.

**Requirements:**

**1. Local Setup:**

Before running the application locally, ensure you have the following Python libraries installed:

```
pip install streamlit google-generativeai PyPDF2 python-dotenv
```

**2. Google Gemini API Key:**

You'll need an API key for the Google Gemini service. Once obtained, store it securely in a dedicated file named `.env` with the following content:

```
GOOGLE_API_KEY=your_api_key_here
```

**How to Run:**

1. **Clone the Repository:**

```
git clone https://github.com/your_username/smart-ats-chatbot.git
cd smart-ats-chatbot
```

2. **Set Up Environment Variables:**

Create a `.env` file in the project directory (if not already present) and add your Google API key as mentioned above.

3. **Run the Streamlit App:**

Start the application using:

```
streamlit run app.py
```

4. **Interact with the Chatbot:**

Upload your resume (PDF) and utilize the chat interface to ask questions and receive insights. The chatbot will provide a Resume Preparation Score, personalized feedback, internship suggestions, and potential job role recommendations.

**Example Interaction:**

**User:** "What can I improve in my resume?"

**ATS:** "Your resume is well-structured, but consider adding more details about your accomplishments and their impact."

**User:** "Can you suggest some internships?"

**ATS:** "Here are some internships relevant to your skills: Python Developer Intern, Data Analyst Intern, Machine Learning Intern."

**User:** "What job roles should I target?"

**ATS:** "Based on your resume, you have the potential for roles like Python Developer, Machine Learning Engineer, or Data Analyst."

**Contribution:**

If you'd like to contribute to the Smart ATS Chatbot, feel free to fork the repository, create a separate branch for your modifications, and submit a pull request. We welcome your improvements and suggestions!

**Acknowledgements:**

* Google Gemini API for AI-powered responses
* PyPDF2 for text extraction from PDFs
* Streamlit for building the web interface
* Regex for analyzing and extracting relevant resume content
