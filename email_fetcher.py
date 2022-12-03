import imaplib
import socket
import time
import traceback

from imap_tools import MailBox, AND, A, U, MailboxLoginError, MailboxLogoutError


class EmailFetcher:
    def __init__(self, imap_config):
        self.imap_config = imap_config

    def fetch_unread_emails(self, folder, callback):
        last_fetch_uid = [0]
        while True:
            try:
                with MailBox(self.imap_config.server).login(self.imap_config.username, self.imap_config.password, folder) as mailbox:
                    for msg in mailbox.fetch(AND(A(seen=False), A(uid=U('%s' % (last_fetch_uid[0] + 1), '*')))):
                        callback(msg)
                        last_fetch_uid[0] = int(msg.uid)
            except (TimeoutError, ConnectionError,
                    imaplib.IMAP4.abort, MailboxLoginError, MailboxLogoutError,
                    socket.herror, socket.gaierror, socket.timeout) as e:
                print(f'## Error\n{e}\n{traceback.format_exc()}\nreconnect in a minute...')
                time.sleep(60)

    def fetch_all_emails(self, folder):
        msgs = []
        with MailBox(self.imap_config.server).login(self.imap_config.username, self.imap_config.password, folder) as mailbox:
            for msg in mailbox.fetch():
                msgs.append(msg)
        return msgs
