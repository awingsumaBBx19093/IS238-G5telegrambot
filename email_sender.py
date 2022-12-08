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
        # in-reply-to and references headers to make it a reply
        msg['Subject'] = msg['Reply-To'] = subject
        msg.add_header("Message-ID", myid)

        """
        testId2 is sample message-id of the message we are replying to.
        I got this message-id from the email headers of the message I am replying to.
        By checking the original message headers of one of the messages in the thread, I found that the message-id is enclosed in angle brackets.
        """
        testId2 = '<167049297946.7756.8723946110605424194@ubuntu-VirtualBox>' 
        
        """
        These are the headers that make it a reply.
        In-Reply-To is the message-id of the message you want to reply to
        References is a list of message-ids of all messages in the thread
        List of message-ids is separated by spaces
        Let us save the message-id of the message we are sending in the References header
        to the database so that we can use it later to reply to the message
        and also add the message-id of the message we are replying to.
        Please note that the message-id of the message we are replying to is not saved in the database yet.
        It will be saved in the database when the message is received by the bot.
        Please help me with this. smiley emoticon
        """

        msg.add_header("In-Reply-To", testId2)
        msg.add_header("References", testId2)

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver, text)
        server.quit()
