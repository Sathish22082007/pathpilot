# 🚀 PathPilot AI  
### AI-Powered Career Guidance System

Turn your resume into a **personalized career roadmap** using AI.

---

## 🧠 Overview

PathPilot AI is an intelligent career assistant that analyzes a user’s resume and provides:

- 🎯 Target role identification  
- 📊 Match score calculation  
- 📉 Skill gap analysis (priority-based)  
- 🗺️ Personalized learning roadmap  
- 💼 Job opportunity recommendations  

It bridges the gap between **learning and employability** by giving users clear, actionable direction.

---

## ✨ Features

### 👤 Profile Extraction
- Extracts structured data from resumes  
- Includes name, email, skills, education, projects, etc.  

### 📊 AI Analysis
- Identifies best-fit role  
- Calculates match score (0–100%)  

### 🧠 Skill Gap Engine
- Categorizes skills into:
  - 🔴 High Priority  
  - 🟡 Medium Priority  
  - 🟢 Low Priority  

### 🗺️ Learning Roadmap
- Step-by-step learning path  
- Includes curated resources (docs, videos, courses)  

### 💼 Opportunities
- Job recommendations  
- Match-based suggestions  
- Skill-aware insights  

---

## ⚙️ How It Works

```
User Uploads Resume
        ↓
n8n Workflow Triggered
        ↓
Ollama (LLM) Processes Resume
        ↓
Django Backend Structures Data
        ↓
Dashboard Displays Insights
```

---

## 🔄 n8n Workflow Overview

PathPilot AI uses **n8n** to automate the resume analysis pipeline and connect AI processing with the backend.

### 🧠 Workflow Purpose

- Receive resume from Django backend  
- Extract text from file  
- Send data to AI model (Ollama)  
- Structure the response into JSON  
- Return results back to backend  

---

## ⚙️ Key Nodes Used

### 1️⃣ Webhook Node
- Entry point of the workflow  
- Receives resume file + target role from backend  

### 2️⃣ File Processing Node
- Extracts text from uploaded resume (PDF/DOCX)  

### 3️⃣ AI (Ollama) Node
- Processes resume text using LLM  
- Extracts:
  - profile details  
  - skills  
  - projects  
  - analysis (role, score, missing skills)  

### 4️⃣ Function / Code Node
- Cleans and structures AI output  
- Ensures valid JSON format  

### 5️⃣ Respond to Webhook Node
- Sends processed data back to Django backend  

---

## 🔁 Workflow Flow

```
Webhook → File Processing → AI (Ollama) → Data Formatting → Response
```

---

## 🖥️ Tech Stack

### Frontend
- HTML, CSS, JavaScript  
- Modern responsive UI  

### Backend
- Django (Python)  

### AI / LLM
- Ollama (local models like `phi3`, `llama3`)  

### Automation
- n8n (workflow orchestration)  

---

## 📸 Screenshots

> Add screenshots here:

- Landing Page  
- Dashboard (Profile / Analysis / Roadmap / Opportunities)  
- n8n Workflow  

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/pathpilot-ai.git
cd pathpilot-ai
```

---

### 2️⃣ Setup Backend

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3️⃣ Run Django Server

```bash
python manage.py runserver
```

---

### 4️⃣ Start Ollama

```bash
ollama serve
```

Install a model:

```bash
ollama pull phi3
```

---

### 5️⃣ Start n8n (Docker)

```bash
docker start n8n
```

Or first time:

```bash
docker run -d \
  --name n8n \
  --network host \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

---

### 6️⃣ Access Services

- Django → http://localhost:8000  
- n8n → http://localhost:5678  
- Ollama → http://127.0.0.1:11434  

---

## 🔧 Configuration

### n8n → Ollama Node

```
Base URL: http://127.0.0.1:11434
Model: phi3 (or llama3)
```

---

## 🚀 Future Improvements

- 🔗 Real-time job API integration  
- 📄 Resume improvement suggestions  
- 🎤 AI interview preparation  
- 📊 Progress tracking system  
- 📱 Mobile application  

---

## 🎯 Impact

PathPilot AI helps users:

- Gain clarity in career direction  
- Focus on relevant skills  
- Reduce time spent on irrelevant learning  
- Improve job readiness  

---

## 🧠 Key Innovation

Unlike generic AI tools, PathPilot AI provides:

> **Structured, personalized, and actionable career guidance**

---

## 🙌 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sathish**  
AI & Full Stack Developer  

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
