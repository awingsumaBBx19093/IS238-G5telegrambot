### Setup

#### install required Python modules
```bash
pip install imap-tools
pip install python-telegram-bot  
pip install pyyaml
```

#### Update application config file
Update the `application.yaml` with correct values:
```yaml
credentials:
  imap:
    server: 'imap.example.com' # make sure IMAP is enabled on the account to integrate
    username: 'your-email@example.com'
    password: 'iamnosecretpassword'
  telegram:
    token: 'your-bot-tg-token'
```
