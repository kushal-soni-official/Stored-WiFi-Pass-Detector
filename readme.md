# Wi‑Fi Profile Password Extractor

A simple Python tool for Windows that lists all stored Wi‑Fi networks (SSIDs) and their saved passwords using the `netsh` command.

## Preview



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


## ⚠️ DISCLAIMER & LEGAL NOTICE

**This tool is for:**
- ✅ Educational purposes to understand system security
- ✅ Testing **on systems you own** only
- ✅ Learning how Windows stores credentials
- ✅ Security researchers and cybersecurity students

**This tool MUST NOT be used for:**
- ❌ Extracting passwords from systems you don't own
- ❌ Unauthorized credential theft
- ❌ Any illegal activity

**Legal Warning:**
Unauthorized credential extraction or theft is a crime under:
- India: Information Technology Act, 2000 (ITA)
- USA: Computer Fraud and Abuse Act (CFAA)
- Most countries have similar cybercrime laws

---

### ⚡ Important
- This is a basic educational tool that demonstrates how Windows stores WiFi credentials
- Use only on your own devices for learning purposes
- **Contributor is NOT responsible for misuse**
