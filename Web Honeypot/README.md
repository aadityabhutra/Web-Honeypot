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

## Security Note

This honeypot is for educational and research purposes only. Do not expose it to the public internet without proper precautions.

## License

MIT License 