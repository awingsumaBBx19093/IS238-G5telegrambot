import smtplib
import email.utils
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

con = sqlite3.connect('chatbotDatabase.db', check_same_thread=False)
cur = con.cursor()

# Declaration of EmailSender class, initializing user’s telegram bot. This script will send the information fed to the bot and will display in the user's UP Gmail inbox. Email responses to the same user and subject will be threaded.
class EmailSender:
    def __init__(self, imap_config):
        self.sender_email = imap_config.username
        self.sender_password = imap_config.password

    def send(self, subject, body, receiver):
        msg = MIMEMultipart()
        myid = email.utils.make_msgid()
        msg['From'] = self.sender_email
        msg['To'] = receiver
        msg['Date'] = email.utils.formatdate(localtime=True)
        msg['Subject'] = msg['Reply-To'] = subject
        msg.add_header("Message-ID", myid)

        # Select the msgIDbot from tblMsgsLogs that corresponds to subject
        cur.execute('''SELECT * FROM tblMsgsLogs where msgIDBot = ?''', (subject,))

        if cur.fetchone() is None:

            msgIDEmail = email.utils.make_msgid()
            # Insert the msgIDbot and msgIDemail into tblMsgsLogs
            cur.execute('''INSERT INTO tblMsgsLogs (msgIDBot, msgIDEmail) VALUES (?, ?)''', (subject, msgIDEmail))
            
        else:
            msgIDEmail = cur.fetchone()[1]
            # Update the msgIDemail in tblMsgsLogs
            cur.execute('''UPDATE tblMsgsLogs SET msgIDEmail = ? WHERE msgIDBot = ?''', (msgIDEmail, subject))
            
        # Execute the commands above
        con.commit()
        
        if msgIDEmail:
            msg.add_header("In-Reply-To", msgIDEmail)
            msg.add_header("References", msgIDEmail)

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver, text)
        server.quit()
