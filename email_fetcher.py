from imap_tools import MailBox, AND, A, U


class EmailFetcher:
    def __init__(self, imap_server, username, password):
        self.imap_server = imap_server
        self.username = username
        self.password = password

    # Fetch unread emails
    def fetch_unread_emails(self, folder, start_uid):
        msgs = []
        with MailBox(self.imap_server).login(self.username, self.password, folder) as mailbox:
            for msg in mailbox.fetch(AND(A(seen=False), A(uid=U('%s' % start_uid, '*')))):
                msgs.append(msg)
        return msgs


    # fetch all emails in plain text - TEST
    def fetch_all_emails(self, folder):
        msgs = []
        with MailBox(self.imap_server).login(self.username, self.password, folder) as mailbox:
            for msg in mailbox.fetch():
                msgs.append(msg)
        return msgs