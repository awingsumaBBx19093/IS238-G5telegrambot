## g5-telegramBot-IS238
Group 5 Main Repository

### Configuaration

#### Required Python modules
```bash
pip install imap-tools
pip install python-telegram-bot  
pip install pyyaml

or 

pip install -r requirements.txt
```

#### Update application config file
Update the `application.yaml` with correct values:
```yaml
credentials:
  imap:
    server: 'imap.example.com' 
    username: 'your-email@example.com'
    password: 'iamnosecretpassword'
  telegram:
    token: 'your-bot-tg-token'
```