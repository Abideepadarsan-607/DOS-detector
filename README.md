# Deauth Attack Detector

## 📌 Description
This Python tool helps detect **Deauthentication (Deauth) Attacks** on a Wi-Fi network by sniffing packets and identifying Deauth frames. Deauth attacks are commonly used for **Wi-Fi denial-of-service (DoS) attacks** and capturing handshake packets for hacking attempts.

## 🚀 Features
- Detects Deauth attack packets in real time.
- Logs attack attempts to a file (`deauth_attack.log`).
- Supports Python 3 with improved error handling.
- User-friendly interface and clean output.

## 🛠 Requirements
- Python 3
- `scapy` library (for packet sniffing)
- A Wi-Fi adapter that supports **monitor mode**

## 🔧 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Deauth_Attack_Detector.git
   cd Deauth_Attack_Detector
   ```
2. Install dependencies:
   ```bash
   pip install scapy
   ```

## ▶️ Usage
1. Run the script as root:
   ```bash
   sudo python3 Deauth_Attack_Detector.py
   ```
2. Enter your network interface (e.g., `wlan0mon`).
3. The tool will start detecting Deauth packets and log them.

## 📝 Example Output
```
[*] Starting Deauthentication Attack Detection...
[+] Deauthentication Packet detected! Count: 1
[+] Deauthentication Packet detected! Count: 2
```

## 🛑 Stopping the Tool
Press `CTRL + C` to stop the tool safely.

## ⚠️ Note
This tool **only detects attacks**; it does not prevent them. If you see repeated alerts, consider improving your Wi-Fi security by:
- Changing your Wi-Fi password.
- Using WPA3 security.
- Disabling SSID broadcasting.

## 📜 License
This project is licensed under the MIT License.

## ✨ Credits
- Developed by **ABIDEEPADARSAN**

## 🌟 Contribute
Feel free to submit issues or pull requests to improve this tool!

## 🔗 Contact
For any queries, reach out via [Gmail](abithor221@gmail.com).


