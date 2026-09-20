# Educational Ransomware Project

⚠️ **WARNING: This is a fully functional ransomware for EDUCATIONAL PURPOSES ONLY** ⚠️

This repository contains a complete ransomware implementation designed for cybersecurity education and research. I am aware that this code could be misused for malicious purposes, but I believe that understanding attack techniques is essential for developing effective defenses.

## Educational Purpose

This project was created to help cybersecurity students, researchers, and professionals:

- Understand how ransomware works from a technical perspective
- Study the propagation mechanisms used by real-world malware
- Develop detection and prevention strategies
- Create effective incident response procedures
- Test security controls and defenses in isolated environments

## Features

- **File Encryption**: AES-256 encryption of files with numerous extensions
- **Cross-platform**: Works on Windows, Linux, and macOS
- **Propagation**: Spreads via email, removable drives, and network shares
- **System Control**: Disables mouse, USB devices, and other peripherals
- **Visual Impact**: Animated ASCII skull art with ransom message
- **Persistence**: Maintains presence on infected systems

## ⚠️ LEGAL DISCLAIMER

This software is provided for EDUCATIONAL AND RESEARCH PURPOSES ONLY. The creators of this software are not responsible for any misuse or damage caused by this software. Users are required to:

- Only run this software in isolated, controlled environments
- Not use this software against any systems without explicit permission
- Comply with all applicable laws and regulations
- Take full responsibility for their actions

## ⚠️ DANGEROUS - DO NOT RUN ON PRODUCTION SYSTEMS

This software will:
- Encrypt your files permanently without proper decryption key
- Disable mouse and USB functionality
- Spread to other systems on your network
- Send itself to your email contacts
- Display persistent ransom messages

## Educational Use Cases

1. **Security Training**: Demonstrate the impact of ransomware attacks
2. **Detection Testing**: Test antivirus and EDR solutions
3. **Incident Response**: Practice containment and recovery procedures
4. **Security Research**: Analyze malware behavior and techniques
5. **Defense Development**: Create and test countermeasures

## Installation (For Controlled Lab Use Only)

```bash
git clone https://github.com/yourusername/educational-ransomware
cd educational-ransomware
chmod +x setup.sh
./setup.sh
