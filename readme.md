# Wi‑Fi Profile Password Extractor

A simple Python tool for Windows that lists all stored Wi‑Fi networks (SSIDs) and their saved passwords using the `netsh` command.

## Features
- Retrieves all Wi‑Fi profiles from the system.
- Displays the password (if available) for each profile.
- Clean tabular output.

## Requirements
- Windows operating system
- Python 3.6 or later
- Administrator privileges (to see actual passwords)

## Installation
1. Download the script `wifi_profiles.py`.
2. No additional libraries are required – it uses only the standard library.

## Usage
1. **Open a Command Prompt as Administrator** (right‑click → “Run as administrator”).
2. Run the script:
   ```cmd
   python wifi_profiles.py