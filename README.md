# **g5-telegramBot-IS238**
*A telegram chatbot that monitors the email of a private group chat run through python code.*

---
## Group 5 Main Repository

### Configuration
#### BOT Creation
1. Create a new telegram bot with BotFather 

You can easily run your own instance of the bot. You can run on any OS (Windows, Mac or Linux). 

1. Open your `CMD` prompt (Windows) or `terminal`(Mac) and follow instructions to run the bot.

   > **Note:** Use python 3.8 or above version

   - Make sure you have `git`, `python` and `pip`.

   ```bash
     # the following commands should not produce error
     git --version
     python --version # 3.8 is recommended
     pip --version
    ```

2. Clone the codes repository and move it into the desired folder.
    ```shell
     git clone https://github.com/dhona101/g5-telegramBot-IS238.git
    ```

3. Install the requirements
   - Required Python modules
   ```bash
     pip install -r requirements.txt
   ```

4. Open any python IDE (e.g., PyCharm, Visual Studio Code, etc.) and locate the folder where the clone code repository is stored.

6. Update the application config file
   - Open the `application.yaml` file and update it with the correct values:
   ```yaml
     credentials:
        imap:
           server: 'imap.example.com' 
           username: 'your-email@example.com'
           password: 'iamnosecretpassword' {email app password recommended}
        telegram:
           token: 'your-bot-tg-token'
    ```

### How to deploy to EC2 instance

1. Create an EC2 instance
2. Install `docker` engine on the created EC2 instance. If chosen Machine Image is **Amazon Linux**, the `scripts/init-server.sh` file 
   can be used to set up everything in that EC2 instance:
   ```bash
   ./scripts/init-server.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
3. Once EC2 instance is set, run `scripts/deploy.sh` to deploy and run the application in the EC2 instance.
   Make sure `application.yaml` is already set with correct credentials and other app-specific configurations:
   ```bash
   ./scripts/deploy.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
   Note: the `deploy` command stops a previous version of the code and starts another instance with the latest changes in the code.

#### Starting and Stopping Application
- To stop the application on a local machine or without manually connecting to remote EC2 instance, run the following command:
   ```bash
   ./scripts/stop.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
   ```
- Similarly, to start the application (only possible if the app was already deployed):
  ```bash
  ./scripts/start.sh path/to/file.pem ec2-user@your-ec2-instance-host.com
  ```
