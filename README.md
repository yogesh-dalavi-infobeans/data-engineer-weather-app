# 🌦️ Weather Data Science Dashboard

A Python-Django application that collects daily weather data for **Kolhapur** using the free **Open-Meteo API**, stores it in **MySQL**, and displays the data in a clean web-based dashboard with charts and filters.

---

## ✅ Features

- 🔁 Automatic weather data collection using CRON
- 🌐 Weather API integration (Open-Meteo - free & no API key)
- 💽 Data stored in MySQL
- 📈 Visual dashboard with charts (Matplotlib)
- 📊 Tabular view using Pandas
- 🧮 Filter options: All Data, Last 7 Days, Last 30 Days

---

## 🧰 Tech Stack

| Technology     | Purpose                         |
|----------------|----------------------------------|
| Python         | Core programming language        |
| Django         | Web framework                    |
| MySQL          | Database                         |
| Pandas         | Data manipulation and table HTML |
| Matplotlib     | Chart generation                 |
| SQLAlchemy     | DB connection engine for Pandas  |
| CRON           | Scheduled job (Linux/Mac)        |
| Open-Meteo API | Free weather data provider       |

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yogesh-dalavi-infobeans/data-engineer-weather-app.git
cd data-engineer-weather-app

