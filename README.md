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

## ✨ Demo Video



https://github.com/user-attachments/assets/51d7b068-cfb2-4b3c-a379-b4b4d210288b


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
- Ollama (local models like `phi3`, `llama3` or cloud models)  

### Automation
- n8n (workflow orchestration)  

---

## 📸 Screenshots

- Landing Page  
<img width="1646" height="1673" alt="Screenshot 2026-04-24 at 22-47-47 PathPilot AI — Engineering Your Future" src="https://github.com/user-attachments/assets/661484c7-9c8d-439a-95f7-c3e87d524ab3" />

- Dashboard (Profile / Analysis / Roadmap / Opportunities)  
<img width="1745" height="1292" alt="Screenshot 2026-04-24 at 22-43-49 Dashboard - PathPilot AI" src="https://github.com/user-attachments/assets/99e5b001-8225-4f60-a702-e6081b3058ac" />

<img width="1752" height="1064" alt="FireShot Capture 077 - Dashboard - PathPilot AI - 127 0 0 1" src="https://github.com/user-attachments/assets/a12a2b71-c6e6-4f0d-acd3-87ce8ff612d6" />

<img width="1752" height="1064" alt="FireShot Capture 078 - Dashboard - PathPilot AI - 127 0 0 1" src="https://github.com/user-attachments/assets/c05a8ba0-e6fc-407d-ace1-5d4a6c3df661" />

<img width="1752" height="1064" alt="FireShot Capture 079 - Dashboard - PathPilot AI - 127 0 0 1" src="https://github.com/user-attachments/assets/8e630acb-bac0-49cb-a852-250554109aec" />

<img width="1752" height="1064" alt="FireShot Capture 081 - Dashboard - PathPilot AI - 127 0 0 1" src="https://github.com/user-attachments/assets/845e3b21-fae1-4b8d-bd0a-6b370d11012c" />

- n8n Workflow

<img width="1751" height="1063" alt="Screenshot 2026-04-24 at 22-51-34 🔄 AI Career Guidance System - n8n" src="https://github.com/user-attachments/assets/625ec901-d895-440c-8c43-c3715919ca5d" />

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
