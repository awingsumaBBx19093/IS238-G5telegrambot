# Importing yaml module
import yaml

# Declaration of Config class, initializing objects to obtain user account credentials, address of remote mail server,
# telegram config and configuration which controls behavior of this script.
class Config:
    def __init__(self, credentials_config, email_fetching_config , send_email_config):
        self.credentials_config = credentials_config
        self.email_fetching_config = email_fetching_config
        self.send_email_config = send_email_config

    @staticmethod
    def load():
        # Load application.yaml
        with open('./application.yaml') as config_file:
            config = config_file.read()
        app_config = yaml.load(config, Loader=yaml.FullLoader)

        return Config(
            CredentialsConfig(
                ImapConfig(
                    app_config["credentials"]["imap"]["server"],
                    app_config["credentials"]["imap"]["username"],
                    app_config["credentials"]["imap"]["password"],
                ),
                TelegramConfig(
                    app_config["credentials"]["telegram"]["token"]
                ),
            ),
            EmailFetchingConfig(
                app_config["email-fetching"]["folder"]
            ),
            sendEmailConfig(
                app_config["send-email"]["subject"]
            ),
        )

    
# Declaration of CredentialsConfig class, initializing and opening linkage to user UP gmail inbox and telegram bot.
class CredentialsConfig:
    def __init__(self, imap_config, telegram_config):
        self.imap_config = imap_config
        self.telegram_config = telegram_config

        
        
# Declaration of ImapConfig class, initializing user’s UP Gmail account
# (fetching the information declared in application.yaml file)
class ImapConfig:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

        
# Declaration of TelegramConfig class, initializing the user's telegram bot’s API token.
class TelegramConfig:
    def __init__(self, token):
        self.token = token

        
# Declaration of EmailFetchingConfig class, initializing user’s UP Gmail Inbox.
# This script will retrieve the mails from Gmail Inbox and will display in telegram bot.
class EmailFetchingConfig:
    def __init__(self, folder):
        self.folder = folder
        
        
# Declaration of sendEmailConfig class, initializing the user's telegram bot.
# This script will send the information fed to the bot and will display in the user's UP Gmail inbox.
# Email responses to the same user and subject will be threaded.
class sendEmailConfig:
    def __init__(self, subject):
        self.subject = subject
