# Security Log Classifier

Python script that reads a login log and writes a short summary.

Each line is a username, an IP, and `SUCCESS` or `FAILURE`. It counts successes and failures, treats addresses starting with `10.` or `192.168.` as internal (the rest as external), and flags any username and IP with three or more failures as a possible brute-force attempt. The report is printed and saved to `summary.txt`.

```bash
python3 security_log_classifier.py
```

It asks for a log filename and uses `logins.txt` if you press Enter.
