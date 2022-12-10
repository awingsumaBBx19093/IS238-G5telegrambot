## g5-telegramBot-IS238
Group 5 Main Repository

### Configuration

#### Required Python modules
```bash
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

### How to Deploy to EC2 Instance

1. Create an EC2 instance
2. Install `docker` engine on the created EC2 instance. If chosen Machine Image is Amazon Linux, the `scripts/init-server.sh` file 
   can be used to set up everything in that EC2 instance:
   ```bash
   ./scripts/init-server.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
3. Once EC2 instance is set, run `scripts/deploy.sh` to deploy and run the application in the EC2 instance.
   Make sure `application.yaml` is already set with correct credentials and other app-specific configuration:
   ```bash
   ./scripts/deploy.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
   Note: the `deploy` command stops a previous version of the code and start another instance with the latest changes in the code.

#### Starting and Stopping Application
- To stop application on local machine or without manually connecting to remote EC2 instance, run the following command:
   ```bash
   ./scripts/stop.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
- Similarly, to start the application (only possible if the app was already deployed):
  ```bash
  ./scripts/start.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
  ```