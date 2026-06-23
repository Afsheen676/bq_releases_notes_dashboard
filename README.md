# 📊 BigQuery Release Notes Dashboard

A fully functional, full-stack web application that fetches live BigQuery release notes from Google's official feed and displays them in an interactive, user-friendly dashboard.

This project was built as part of the **Kaggle x Google 5-Day AI Agents Intensive Course** to demonstrate proficiency in Python, Flask, API integration, and frontend development.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **📡 Live Data Fetching** | Automatically retrieves the latest BigQuery updates directly from Google's official XML feed. |
| **🔄 Smart Refresh** | One-click refresh button with a dynamic loading spinner to fetch the newest updates without reloading the page. |
| **✅ Interactive Selection** | Click on any update card to select/unselect it. Selected cards are visually highlighted. |
| **🐦 Twitter Integration** | Compile selected updates and post them instantly to Twitter/X via a single click. |
| **🎨 Modern UI** | Clean, responsive design with a dark header, card-based layout, and smooth hover/click animations. |
| **⚡ Real-time Status** | Displays a live status message showing when the data was last updated. |

---

## 🧠 Architecture & Data Flow

Understanding how the app works:
[Google Servers]
│
│ (1) Fetches XML Feed
▼
[Flask Backend (app.py)]
│
│ (2) Parses XML & Converts to JSON
▼
[API Endpoints (/api/notes)]
│
│ (3) Sends JSON Data to Frontend
▼
[Browser Frontend (index.html)]
│
│ (4) JavaScript Renders Interactive Cards
▼
[User Dashboard]

text

### Step-by-Step Breakdown

1. **User Request**: You open `http://127.0.0.1:5000` in your browser.
2. **Serving the Page**: Flask receives the request and sends the `index.html` file to your browser.
3. **JavaScript Initialization**: The browser loads the HTML, CSS, and JavaScript. The JavaScript immediately calls the `load()` function.
4. **API Call**: `load()` makes a `fetch()` request to the `/api/notes` endpoint on your Flask server.
5. **Backend Processing**:
   - Flask uses the `requests` library to download the BigQuery XML feed from Google.
   - Flask parses the XML using `xml.etree.ElementTree` to extract `title`, `summary`, `published date`, and `link` from each entry.
   - The extracted data is converted into a JSON array.
6. **Frontend Rendering**:
   - The JavaScript receives the JSON data.
   - It loops through each note and dynamically creates HTML `<div>` cards.
   - The cards are inserted into the `notesContainer` div.
7. **User Interaction**:
   - **Refresh**: You click "Refresh" → JavaScript calls `/api/refresh` → Repeats steps 4-6.
   - **Select**: You click a card → JavaScript toggles a "selected" state and updates the UI.
   - **Tweet**: You click "Tweet Selected" → JavaScript grabs the selected titles and opens a new Twitter window with a pre-filled message.

---

## 📂 Detailed Folder & File Structure
bq_releases_notes_dashboard/
│
├── app.py # 🐍 Flask Backend (Server)
├── templates/
│ └── index.html # 🌐 Frontend (HTML + CSS + JS)
├── static/
│ └── style.css # 🎨 Extra Styling (Linked but optional)
├── README.md # 📄 This file
└── .gitignore # 🚫 Ignored files (cache, .env, etc.)

text

### File Responsibilities

| File | Role | Key Components |
| :--- | :--- | :--- |
| **`app.py`** | **Backend Logic** | `FEED_URL` (Google's XML link), `fetch_notes()` (downloads/parses XML), `/api/notes` (JSON endpoint), `/api/refresh` (refresh endpoint), `/` (serves HTML). |
| **`index.html`** | **User Interface** | `<header>` (Title & Buttons), `<div id="notesContainer">` (Card holder), `<style>` (Embedded CSS), `<script>` (Fetch logic, render logic, selection logic). |
| **`style.css`** | **Styling Extension** | (Optional) Contains all the CSS rules for colors, shadows, borders, and responsive design. |

---

## 🛠️ Full Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Language** | **Python 3** | Handles server logic, API requests, and data parsing. |
| **Web Framework** | **Flask** | Lightweight framework for routing, serving HTML, and creating REST APIs. |
| **HTTP Client** | **Requests** | Makes the external call to Google's servers to fetch the XML feed. |
| **XML Parser** | **xml.etree.ElementTree** | Built-in Python library that converts XML data into a readable tree structure. |
| **Frontend** | **HTML5, CSS3, JavaScript** | Builds the visual layout, styling, and interactivity (click, refresh, tweet). |
| **Version Control** | **Git & GitHub** | Tracks changes, manages code history, and hosts the project remotely. |
| **Runtime** | **Flask Development Server** | Runs the app locally on `http://127.0.0.1:5000`. |

---

## 🔌 API Endpoints Explained

Your Flask app exposes these endpoints for the frontend to consume:

| Endpoint | Method | Description | Example Response |
| :--- | :--- | :--- | :--- |
| `/` | GET | Serves the main HTML page. | Renders `index.html` |
| `/api/notes` | GET | Fetches and returns the latest BigQuery release notes in JSON format. | `[{"title": "...", "summary": "...", "published": "...", "link": "..."}]` |
| `/api/refresh` | GET | Same as `/api/notes`, used specifically for the refresh button. | `[{"title": "...", ...}]` |

---

## 🚀 How to Run This Project Locally

Follow these steps to get the app running on your own machine:

**1. Clone the repository**
```bash
git clone https://github.com/your-username/bq_releases_notes_dashboard.git
cd bq_releases_notes_dashboard
2. Install the required dependencies

bash
pip install flask requests
3. Start the Flask server

bash
python app.py
4. Open the app in your browser

text
http://127.0.0.1:5000
⚠️ Note: Keep the PowerShell/terminal window open while running the app. Press CTRL+C to stop the server.

**🌐 Live Demo:** [https://bq-releases-notes-dashboard.onrender.com](https://bq-releases-notes-dashboard.onrender.com)
👤 About the Author
Afsheen Muavia
BS Data Science (2nd Semester)
Islamia University of Bahawalpur, Baghdad Campus

I am a passionate Data Science student with a strong interest in AI, Machine Learning, and Web Development. This project reflects my ability to build real-world applications by combining Python, APIs, and modern web technologies.

GitHub: https://github.com/Afsheen676

LinkedIn: https://linkedin.com/in/www.linkedin.com/in/afsheen-muavia-a423113a8

Email: beenm126@gmail.com

📅 Project Context
Course: Kaggle x Google 5-Day AI Agents Intensive Course (June 2026)

Objective: Build a functional web application using Python Flask and AI-assisted development tools (Antigravity CLI).

Timeline: Completed within 2 days (June 22-23, 2026).

📜 License
This project is for educational and portfolio purposes only. You are free to use, modify, and distribute it for learning.

⭐ If you found this project helpful, please consider giving it a star on GitHub! ⭐

text

---



