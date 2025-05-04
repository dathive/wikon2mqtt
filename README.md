# Wikon2MQTT

## 🛢️ Wikon to Home Assistant via MQTT

This project retrieves gas tank data from Wikon platform (level and forecast) using Selenium, then publishes it daily to Home Assistant via MQTT.

⚠️ This script scrapes data from a personal Wikon account. Please ensure that you comply with Wikon’s terms of service. The authors of this project are not affiliated with Wikon.

---

### ⚙️ Prerequisites

Before running this project, make sure you have:

* ✅ A running instance of **[Home Assistant](https://www.home-assistant.io/)**
* ✅ An **MQTT broker** accessible by Home Assistant (e.g. [Mosquitto](https://mosquitto.org/))

---

### 📦 Overview

* Web scraping using headless Selenium Chrome
* MQTT publishing with `retain=True` (so Home Assistant remembers the last value)
* Scheduled execution every day at 09:00
* Fully containerized using Docker + `docker-compose`

---

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone <repo_url>
cd wikon2mqtt
```

#### 2. Create the environment file

Create a `.env` file at the root of the project:

```env
MQTT_BROKER=localhost
MQTT_PORT=1883
MQTT_TOPIC=home/wikon
SELENIUM_URL=http://selenium:4444/
WIKON_URL=http://wikon-url/
WIKON_USERNAME=your_username
WIKON_PASSWORD=your_password
```

#### 3. Start the stack

```bash
docker compose up --build -d
```

This will launch:

* `app` – the main Python script
* `selenium` – headless Chrome browser

---

### 🧠 How It Works

* The script runs daily at **09:00** (configured with `schedule`).
* It opens a headless Selenium session, logs into Wikon, extracts tank level and forecast.
* The data is published to MQTT using `retain=True` so that Home Assistant keeps the last known value even if the script stops.

---

### 📄 Project Structure

```
.
├── config.py            # Loads environment variables
├── main.py              # Main script with scheduler
├── mqtt_client.py       # MQTT publishing class
├── wikon.py             # Wikon scraping class using Selenium
├── requirements.txt     # Python dependencies
├── Dockerfile           # Python image
├── docker-compose.yml   # Multi-container deployment
├── .env                 # Environment file (excluded from git)
└── README.md
```

---

### 🧪 Manual Test

You can trigger the script manually (instead of waiting for 09:00):

```bash
docker compose exec app python main.py
```

---

### 🏠 MQTT in Home Assistant

If MQTT discovery is enabled, the sensors will appear automatically.
Otherwise, you can add them manually:

```yaml
sensor:
  - name: "Gas Tank Level"
    state_topic: "home/wikon/tank_level"
    unit_of_measurement: "%"
  - name: "Forecast"
    state_topic: "home/wikon/forecast"
    unit_of_measurement: "days"
```

---

### 🔐 Security

* Store your `.env` file securely and never commit it.
* Use authentication on your MQTT broker if exposed to the internet.
* Rotate Wikon credentials periodically.

---

### 🧼 To-Do / Ideas

* [ ] CSV or log export
* [ ] Notifications on failure
* [ ] Healthchecks / Watchtower monitoring
