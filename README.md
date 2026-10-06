# 🤖 OMNI AI

> **A Local AI-Powered Multi-Purpose Assistant built with Python, Streamlit, and Ollama**

OMNI AI is a local AI assistant designed to provide multiple AI-powered features through a simple and user-friendly Streamlit interface.

The project uses **Ollama** to run an AI model locally on your computer, so the application does not require OpenAI API credits for its AI responses.

---

## 🚀 Features

### 💬 AI Chat

* Chat with a local AI model
* Maintains conversation history
* Simple and user-friendly interface
* No cloud API required

### 📄 Document AI

Planned features:

* Upload PDF files
* Upload DOCX files
* Upload TXT files
* Ask questions about documents
* Extract useful information

### 📝 AI Summarizer

Planned features:

* Summarize text
* Summarize documents
* Short, medium, and detailed summaries

### 🌐 Translator

Planned features:

* Translate text between languages
* Support multiple languages

### 💻 Code Assistant

Planned features:

* Explain code
* Find programming errors
* Debug code
* Optimize code
* Generate code
* Add comments

### 🧠 AI Memory

Planned features:

* Conversation history
* Persistent user memory
* Context-aware conversations

---

# 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python 3.11   | Main programming language |
| Streamlit     | Web interface             |
| Ollama        | Local AI runtime          |
| Llama 3.2     | Local language model      |
| Requests      | Communication with Ollama |
| python-dotenv | Environment configuration |
| PyPDF         | PDF processing            |
| python-docx   | DOCX processing           |
| Pandas        | Data processing           |
| OpenPyXL      | Excel processing          |
| SQLite        | Planned database          |

---

# 📁 Project Structure

```text
omni ai/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── core/
│   ├── __init__.py
│   ├── ai_engine.py
│   ├── memory.py
│   └── prompts.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── modules/
│   ├── chatbot.py
│   ├── document_qa.py
│   ├── summarizer.py
│   ├── translator.py
│   └── code_assistant.py
│
├── utils/
│   ├── file_handler.py
│   └── helpers.py
│
├── data/
│   └── uploads/
│
└── assets/
    └── logo.png
```

---

# 💻 System Requirements

Before running OMNI AI, make sure your computer has:

* Windows 10/11
* Python 3.11
* VS Code
* Ollama
* At least 8 GB RAM recommended
* Sufficient disk space for the AI model

More powerful hardware will provide faster local AI responses.

---

# ⚙️ Installation

## 1. Clone or download the project

Open the project folder in VS Code.

```powershell
cd "C:\Users\Nanvitha\OneDrive\Desktop\omni ai"
```

---

## 2. Create a Python virtual environment

Use Python 3.11:

```powershell
py -3.11 -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

# 📦 Install Python Dependencies

Run:

```powershell
python -m pip install --upgrade pip
```

Then:

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not ready yet, install the basic packages:

```powershell
pip install streamlit requests python-dotenv pypdf python-docx pandas openpyxl
```

---

# 🧠 Install Ollama

Download and install Ollama on Windows.

After installation, check:

```powershell
ollama --version
```

If a version number appears, Ollama is installed successfully.

---

# 🤖 Download the Local AI Model

For the current OMNI AI configuration:

```powershell
ollama run llama3.2:1b
```

The first run downloads the model.

After downloading, test it:

```text
He
```
