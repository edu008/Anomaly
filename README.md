# Network Anomaly Detection

This project is a Python-based network anomaly detection tool that monitors network traffic in real time, detects anomalies based on predefined thresholds, and logs the data for further analysis.

## Features
- **Packet Monitoring:** Tracks incoming and outgoing network packets.
- **Anomaly Detection:** Detects anomalies such as:
  - High packet rates from a single IP address.
  - Unusual port usage.
  - High number of unique connections.
- **Real-time Alerts:** Alerts are logged and displayed for detected anomalies.
- **Traffic Summary:** Maintains a detailed summary of network activity.
- **JSON Logging:** Logs all alerts and traffic summaries into a JSON file.
- **User Interface:** Includes a simple UI to start and stop monitoring.

## Prerequisites

### Install Required Libraries
Before running the application, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Project Structure
```
Anomaly/
├── core/
│   ├── anomaly_detection.py   # Core anomaly detection logic
│   ├── logger.py              # Logging utility
├── log/
│   └── network_activity.log   # Log file for network activity
├── main.py                    # Entry point for the application
├── README.md                  # Documentation
└── requirements.txt           # Python dependencies
```

## Usage
### 1. Clone the Repository
```bash
git clone <repository-url>
cd Anomaly
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

### 4. Generate Network Activity
You can simulate network activity using tools like `ping`, `curl`, or `nmap`.

### 5. Stop Monitoring
Click the **Stop Monitoring** button on the UI to stop monitoring and save logs.

## Configuration
You can configure thresholds and commonly used ports in `anomaly_detection.py`:
```python
# Thresholds for anomaly detection
THRESHOLD_PACKETS_PER_SECOND = 100
THRESHOLD_UNIQUE_CONNECTIONS = 50
COMMON_PORTS = {80, 443, 22, 21, 25, 110, 445}
```

## Logs
Logs are saved in the `log/` directory in JSON format.
