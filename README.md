# BigQuery Release Notes Dashboard 📊

A Flask web application that fetches live BigQuery release notes from Google's official feed and displays them in a clean, interactive dashboard.

## ✨ Features

- **Live Feed**: Fetches the latest BigQuery updates from Google's official feed.
- **Refresh Button**: Updates the list with a loading spinner.
- **Select Updates**: Click on any note to select/unselect it.
- **Tweet Integration**: Tweet selected updates with one click.
- **Clean UI**: Simple, modern, and responsive design.

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Backend logic and API integration |
| **Flask** | Web framework for routing and server |
| **HTML** | Page structure |
| **CSS** | Styling and layout |
| **JavaScript** | Interactivity (refresh, select, tweet) |
| **Requests** | Fetching data from Google's feed |
| **XML Parsing** | Reading and parsing Google's release notes feed |

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bq_releases_notes_dashboard.git
cd bq_releases_notes_dashboard