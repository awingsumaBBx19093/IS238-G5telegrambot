import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, imap_config):
        self.sender_email = imap_config.username
        self.sender_password = imap_config.password

    def send(self, subject, body, receiver):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver, text)
        server.quit()