import yaml


class Config:
    def __init__(self, credentials_config, email_fetching_config):
        self.credentials_config = credentials_config
        self.email_fetching_config = email_fetching_config

    @staticmethod
    def load():
        # Load application.yaml
        with open('application.yaml') as config_file:
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
        )


class CredentialsConfig:
    def __init__(self, imap_config, telegram_config):
        self.imap_config = imap_config
        self.telegram_config = telegram_config


class ImapConfig:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password


class TelegramConfig:
    def __init__(self, token):
        self.token = token


class EmailFetchingConfig:
    def __init__(self, folder):
        self.folder = folder
