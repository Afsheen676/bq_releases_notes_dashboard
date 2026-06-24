# Implementation Plan: BigQuery Release Notes Dashboard

## 1. Project Goal
Build a web application that fetches live BigQuery release notes from Google's official feed and displays them in an interactive dashboard with refresh, selection, and tweet functionality.

## 2. Technologies Used
- **Backend**: Python 3, Flask, Requests, XML Parser
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Version Control**: Git, GitHub

## 3. Implementation Steps

### Phase 1: Setup
- [x] Created project folder: `C:\Users\dell\agy_cli_projects\bq-releases-notes`
- [x] Created subfolders: `templates/` and `static/`

### Phase 2: Backend Development
- [x] Created `app.py` with Flask server
- [x] Added `fetch_notes()` function to:
  - Download XML from `https://cloud.google.com/feeds/bigquery-release-notes.xml`
  - Parse XML using `xml.etree.ElementTree`
  - Extract title, summary, date, and link from each entry
- [x] Created API endpoints:
  - `/` → Serves `index.html`
  - `/api/notes` → Returns JSON data
  - `/api/refresh` → Refreshes data

### Phase 3: Frontend Development
- [x] Created `templates/index.html` with:
  - Header with title, refresh button, and tweet button
  - Dynamic card container for notes
  - Loading spinner animation
- [x] Added JavaScript functions:
  - `load()` → Fetches notes on page load
  - `render()` → Displays notes as cards
  - `toggle()` → Select/unselect notes
  - `refreshNotes()` → Fetches latest data with spinner
  - `tweetSelected()` → Opens Twitter with selected titles

### Phase 4: Styling
- [x] Added embedded CSS for:
  - Clean card-based layout
  - Hover effects and transitions
  - Selected state (blue border)
  - Spinner animation

### Phase 5: Testing & Debugging
- [x] Fixed feed URL (updated to correct Google endpoint)
- [x] Added sample data to test UI when feed is unavailable
- [x] Verified refresh, selection, and tweet features

### Phase 6: Deployment & Version Control
- [x] Initialized Git repository
- [x] Created `.gitignore` (to exclude cache files)
- [x] Pushed to GitHub (public repository)
- [x] Added detailed README.md with project documentation

## 4. File Structure 
|agy_cli_projects/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend
├── static/
│ └── style.css # (Optional styling)
├── README.md # Project documentation
├── .gitignore # Ignored files
└── implementation_plan.md # This file
## 5. Future Enhancements (Next Steps)
- Add a "Copy to Clipboard" button for each note
- Add an "Export to CSV" feature
- Add Dark/Light mode toggle
- Deploy the app to a public hosting service (Render, PythonAnywhere)

## 6. Author
**Afsheen Muavia**
- Course: Kaggle x Google 5-Day AI Agents Intensive Course (2026)
- GitHub: https://github.com/Afsheen676