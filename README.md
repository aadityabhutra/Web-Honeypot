# Honeypot Web Application

This project is a simple honeypot built with Flask. It is designed to attract, log, and analyze unauthorized or suspicious access attempts to fake endpoints.

## Features

- Fake endpoints for login, admin panel, API, and files.
- Logs all access attempts with details (timestamp, IP, method, path, payload, user agent).
- Scripts to analyze and visualize attack data.

## Files

- `app.py`: The main Flask honeypot server.
- `attack_analysis.py`: Script to analyze attack logs by path and IP.
- `plot_attacks.py`: Script to visualize attack attempts by path.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Install Dependencies

```bash
pip install flask matplotlib
```

### Run the Honeypot Server

```bash
python app.py
```

The server will start on port 80. You may need to run as administrator or use a different port.

### Analyze Attack Logs

To print attack counts by path and IP:

```bash
python attack_analysis.py
```

### Visualize Attack Data

To generate a bar chart of attack attempts by path:

```bash
python plot_attacks.py
```

This will save a plot as `attack_plot.png`.

## MITRE ATT&CK Coverage

The fake endpoints in this honeypot correspond to real-world Initial Access techniques:

| Fake Endpoint | Simulates | ATT&CK ID |
|---|---|---|
| /login | Credential access attempts | T1078 |
| /admin | Admin panel exploitation | T1098 |
| /api/data | API abuse / data exfiltration | T1530 |
| /files | File access / web shell attempts | T1505.003 |


## Deployment Notes

Designed for deployment on a cloud VPS or AWS EC2 instance with a public IP. To maximise data collection, expose ports 80/443. For responsible deployment: run inside an isolated VPC, restrict outbound traffic, and rotate your instance every 72 hours to avoid becoming part of an attack infrastructure. All captured data should be treated as potentially hostile — do not execute any payloads from logs.

## License

MIT License 
