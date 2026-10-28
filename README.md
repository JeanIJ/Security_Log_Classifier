# Security Log Classifier

Python script that summarizes login logs and flags possible brute-force patterns.

## Description
Reads login log lines (user, IP, SUCCESS/FAILURE), counts successes and failures, classifies internal vs external IPs, and flags user+IP pairs with three or more failures as possible brute force. Writes a summary report.

## Technologies
- Python 3

## Usage
```bash
python3 security_log_classifier.py
```

## Status
Completed learning exercise.
