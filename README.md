# 🌦️ Weather Data Science Dashboard

A Python-Django application that collects daily weather data for **Pune** using the free **Open-Meteo API**, stores it in **MySQL**, and displays the data in a clean web-based dashboard with charts and filters.

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
```

### 2. Install Python Dependencies

Use the `requirements.txt` provided:

```bash
pip install -r requirements.txt
```
### 3. Configure Django
```aiignore
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weather_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
### 4. Automate Daily Weather Collection

1. Create the CRON Job (Linux/macOS):
Open your crontab:
```crontab -e```
Add this line to run at 8:00 AM daily:

```aiignore
0 8 * * * /usr/bin/python3 /full/path/to/weather_collector.py >> /full/path/to/logs/weather.log 2>&1
```
Make sure:

Python path is correct (which python3)

weather_collector.py has correct file path
