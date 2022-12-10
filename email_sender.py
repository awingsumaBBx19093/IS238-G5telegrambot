import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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

        #  TODO: Database to store message id and subject
        # This area here is for testing purposes

        testId2 = '<CADMDgSm+AcFQD+QEGF_YPtqLviE0Wsnmtof8DdMBzZrLrxTYgws@mail.gmail.com>' 

        msg.add_header("In-Reply-To", testId2)
        msg.add_header("References", testId2)

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver, text)
        server.quit()
