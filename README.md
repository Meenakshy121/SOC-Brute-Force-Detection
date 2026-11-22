# SSH Brute Force Attack Detection and Log Analysis

## Project Overview

This project demonstrates basic Security Operations Center (SOC)
activities by analyzing simulated SSH authentication logs to
identify possible brute-force attacks.

The project uses Linux command-line tools and Python to detect
repeated failed login attempts from suspicious IP addresses.

## Objectives

- Analyze authentication logs
- Identify suspicious IP addresses
- Detect repeated failed login attempts
- Create a basic detection rule
- Generate automated alerts using Python
- Document security investigation findings

## Tools Used

- Kali Linux
- Linux Command Line
- Python 3
- Regular Expressions
- Git and GitHub

## Detection Logic

The detection script counts failed SSH login attempts
from each source IP address.

Detection Threshold:

5 or more failed login attempts.

## Test Results

| IP Address | Failed Attempts | Result |
|------------|-----------------|--------|
| 192.168.1.50 | 10 | Possible Brute Force Attack |
| 192.168.1.60 | 3 | Normal |

## Project Files

- auth.log - Simulated SSH authentication logs
- detection-rule.txt - Detection logic
- timeline.txt - Incident timeline
- incident-report.txt - Investigation report
- detect_bruteforce.py - Automated detection script

## Investigation Findings

The analysis identified repeated failed SSH login
attempts from IP address 192.168.1.50.

The source attempted to access multiple accounts,
including admin, root, test, and guest.

The Python script generated an alert because the
source exceeded the detection threshold.

## Disclaimer

This project uses simulated log data for educational
purposes. It does not involve attacking real systems.
