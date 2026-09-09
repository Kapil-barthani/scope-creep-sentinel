# ? AI Scope-Creep Sentinel & Commercial Change Order Engine

> **Protect agency profitability, catch unbilled drift in real-time, and automate professional commercial Change Orders using Gemini AI.**

---

## ?? Live Demo
- **Live Frontend on GitHub Pages:** \https://<your-username>.github.io/<repo-name>/\
- *(Visitors can immediately try the **? Instant Demo** without needing a local backend!)*

---

## ?? Overview

Software consultancies and freelance teams lose thousands in unbilled engineering hours from gradual **scope creep**—seemingly small requests buried in Slack messages or emails (*"Can we also add Apple Sign-In and Crypto checkout before launch?"*).

**AI Scope-Creep Sentinel** acts as a technical solutions architect and commercial director:
1. **Audits Client Requests:** Compares incoming emails against the signed Statement of Work (SOW).
2. **Classifies Scope Status:** Categorizes each item as \IN_SCOPE\, \PARTIAL_EXTENSION\, \OUT_OF_SCOPE\, or \NEEDS_CLARIFICATION\ with contractual clause citations.
3. **Financial Estimation:** Calculates exact engineering drift days and incremental cost using blended daily rates (supporting both **USD \$** and **PKR Rs**).
4. **Negotiation Assistant:** Generates diplomatic, firm, or flexible client reply emails.
5. **Change Order Generator:** Produces formal, downloadable Markdown Change Orders (CRs) ready for client signature.

---

## ??? Architecture

\\\
+-------------------------------------------------------------+
¦              Frontend (GitHub Pages / Local)                ¦
¦       React 18 + Tailwind CSS + Glassmorphism Dark UI       ¦
¦  - Instant Sample Demo Mode (No backend required)           ¦
¦  - Configurable Backend URL (Render / Railway / Localhost)  ¦
+-------------------------------------------------------------+
                               ¦ POST /api/analyze
                               ?
+-------------------------------------------------------------+
¦                 Backend (FastAPI + Uvicorn)                 ¦
¦              Python 3.10+ / Render / Railway                ¦
¦  - Strict Pydantic v2 JSON Schema Enforcement               ¦
¦  - Multi-tier Gemini Flash Fallback Engine                  ¦
¦  - Security Delimiter Guarding against prompt injection     ¦
+-------------------------------------------------------------+
                               ¦
                               ?
+-------------------------------------------------------------+
¦                   Google Gemini 3.6 Flash                   ¦
¦        Contract Analysis & Commercial Drift Reasoning       ¦
+-------------------------------------------------------------+
\\\

---

## ?? Quick Start (Local Run)

### Prerequisites
- Python 3.10+ installed
- A Google Gemini API Key ([Get one free on Google AI Studio](https://aistudio.google.com/))

### 1. Clone & Setup Backend
\\\ash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
\\\

### 2. Configure Environment Variables
Copy the template and add your Gemini API Key:
\\\ash
cp .env.example .env
\\\

Edit \ackend/.env\:
\\\ini
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=gemini-3.6-flash
HOST=0.0.0.0
PORT=8000
\\\

### 3. Start the Server
\\\ash
python main.py
\\\
The application will be live at:
- **UI & API:** [http://localhost:8000](http://localhost:8000)
- **Interactive Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## ?? Deploying to GitHub (Public Showcase)

### 1. Push Code to GitHub
\\\ash
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
\\\

### 2. Enable GitHub Pages (Frontend)
1. Go to your repository on GitHub.
2. Click **Settings** > **Pages** (in the left sidebar).
3. Under **Build and deployment > Source**, select **GitHub Actions**.
4. The included automated workflow (\.github/workflows/deploy.yml\) will automatically build and publish your frontend to:
   \\\
   https://<your-username>.github.io/<repo-name>/
   \\\

### 3. Deploy Backend for Free (Render.com)
Because GitHub Pages only hosts static files (HTML/CSS/JS), host the Python FastAPI backend on Render:
1. Sign up for free at [Render.com](https://render.com/).
2. Click **New +** > **Web Service**.
3. Select your GitHub repository.
4. Configure the service:
   - **Root Directory:** \ackend\
   - **Environment:** \Python 3\
   - **Build Command:** \pip install -r requirements.txt\
   - **Start Command:** \uvicorn main:app --host 0.0.0.0 --port \\
5. Under **Environment Variables**, add:
   - \GEMINI_API_KEY\ = \your_gemini_api_key\
   - \ALLOWED_ORIGINS\ = \*\
6. Click **Create Web Service**.
7. Copy your deployed Render URL (e.g., \https://scope-sentinel.onrender.com\).
8. Open your GitHub Pages site, click **?? API Settings**, paste your Render URL, and click **Save & Apply**!

---

## ?? Repository Structure

\\\
scope-creep-project/
+-- .github/
¦   +-- workflows/
¦       +-- deploy.yml          # GitHub Actions workflow for Pages deployment
+-- backend/
¦   +-- .env.example            # Environment configuration template
¦   +-- main.py                 # FastAPI application & Gemini integration
¦   +-- requirements.txt        # Python backend dependencies
+-- frontend/
¦   +-- index.html              # React 18 + Tailwind UI with Instant Demo mode
+-- .gitignore                  # Git ignore protecting .env and build artifacts
+-- index.html                  # Root forwarder for GitHub Pages
+-- README.md                   # Documentation & deployment guide
\\\

---

## ??? Security & Privacy
- **API Keys are Never Stored in Frontend:** The client connects to the backend over standard CORS.
- **Git Protection:** \.gitignore\ explicitly ignores all \.env\ files to prevent API key leaks.
- **Delimiter Shielding:** Contracts and emails are wrapped in XML delimiters to prevent prompt injection manipulation.

---

## ?? License
Distributed under the MIT License.
