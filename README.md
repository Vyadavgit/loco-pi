# loco-pi
## Steps to run the program
### Tools required
- Raspberry Pi
- TODO
### Generate certs
This script enables SSL context for the API by generating a self-signed SSL certificate and key using OpenSSL.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

The generated certificate and key files, cert.pem and key.pem, are then used to configure the SSL context in the Flask application.

The API provides two routes:
- /start: Starts a separate process by executing the 'main.py' script using the subprocess module.
- /stop: Terminates the running process if it exists.

To run the API, execute this script directly.

Note: Make sure to have OpenSSL installed on your system before running this script.
### Create virtual env
- Navigate to your project's directory:
    ```
    cd /path/to/your/project
    ```
- Create a new virtual environment. Replace env with the name you want to give to your virtual environment:
    ```
    python3 -m venv env
    ```
- Activate the virtual environment:
    ```
    source env/bin/activate
    ```
- Install the packages from requirements.txt
    ```
    pip install -r requirements.txt
    ```
- Run the program. It exposes '/start' and '/stop' trigger APIs. Triggers for the start and stop APIs can be access through index.html page at https://raspberry-pi-IP:PORT/
    ```
    python3 api.py
    ```
#### Deactivate or remove venv
- Run the command below to deactivate venv, if it is already activated
    ```
    deactivate
    ```
- remove venv 
    ```
    rm -rf <venv name>
    ```

### Configure SSH (Secure Shell) for remote access to Raspberry Pi. Programs can be triggered easily using ssh. 
1. Enable SSH on Raspberry Pi:

    You can enable SSH through Raspberry Pi Configuration Settings.

    - Go to the Raspberry Pi Start Menu -> Preferences -> Raspberry Pi Configuration.
    - In the Interfaces tab, ensure SSH is Enabled.
    - Alternatively, you can enable SSH from the terminal: 
        ```
        sudo raspi-config
        ```
        Navigate to Interfacing Options -> SSH and enable it.

2. Secure your Raspberry Pi:
If you're planning to expose your Raspberry Pi to the internet, it's important to secure it. At a minimum, you should change the default password for the pi user. You can do this with the ```passwd``` command: 
    ```
    passwd
    ```
3. Access Raspberry Pi from a remote computer:
On your remote computer, open a terminal (or Command Prompt on Windows), and use the ssh command to connect to your Raspberry Pi:
    ```
    ssh pi@raspberry_pi_ip
    ```
    Run command ```hostname -I``` for IP address of your Raspberry Pi. Replace raspberry_pi_ip with the IP address. You'll be prompted to enter the password for the pi user.
4. Run the program:
    Configure and activate venv and simply run ```python3 main.py``` to trigger the program.
5. Type ```exit``` or ```logout``` and press Enter. This is the standard way to end an SSH session.
6. Run command `sudo shutdown -h now` to shutdown raspberrypi.