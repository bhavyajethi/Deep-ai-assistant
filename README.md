# **Deep Research AI Assistant**

A powerful AI assistant that performs **deep web research** using **Google Gemini**, provides voice interaction, translates answers, and allows one-click PDF export with sources. Perfect for students, researchers, and professionals who want fast, factual, and accessible information.

## **Features**
### Intelligent Research
- Uses **Gemini 1.5 Flash** to generate high-quality, factual answers to user queries.
- Optional web source links shown using a search API.

### Voice Chat Support
- Speak your query using a microphone.
- The assistant listens, understands, and answers using voice (Text-to-Speech).
  
### Translation
- Translate Gemini's answers into Hindi (or other languages if needed).

### Export to PDF
- Save your question, answer, and all cited sources into a well-formatted `output.pdf`.

### Chat History
- Displays previously asked questions and answers for easy reference.

---


# **Tech Stack**

1. **Programming Languages**: 
   - Python

2. **Libraries and Tools**:
   - **Streamlit**: For building the web application.
   - **Googlegenerativeapi**: For researching the ans.
   - **Serperapi**: For the retrieval of news source links relevant to the ques.
   - **Googletrans**: For english to hindi translation.
   - **fpdf**: To save the ans as a pdf.
  
   ## **Prerequisites**

Ensure the following are installed:

- langchain
- langgraph
- langchain-google-genai
- tiktoken
- python-dotenv
- googletrans
- fpdf
- speech_recognition
- pyttsx3
- serper

  
---

## **Setup instructions**

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/bhavyajethi/Deep-ai-assistant.git
   cd Deep-ai-assistant

2. **Set Up Virtual Environment**:  
   ```bash
   python -m venv venv
   venv\Scripts\activate        # On Windows
   # OR
   source venv/bin/activate     # On macOS/Linux


3. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   
4. **Add Your API Keys**:
Create a .env file in the root folder and add:
   ```bash
   GOOGLE_API_KEY=your_gemini_api_key_here
   SERPER_API_KEY=your_web_search_api_key_here     
   .env is ignored by Git for safety.

5. **Run the streamlit Application**:  
   ```bash
   streamlit run app.py
