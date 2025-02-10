# <h2 align=center>Gaianet-BOT by CryptoAirdropHindi</h2>


## 1. Clone the repository to your local machine:
```
git clone https://github.com/Veyronixx/gaianet-bot1.git
cd Gaianet-BOT
```
## 2. Install Python 3: Install Python 3 using the `apt` package manager:
```
sudo apt update
sudo apt install python3
```

## 3. Install `python3-pip` Install `pip` for Python 3 by running:
```
sudo apt install python3-pip
```
## 4. Install the required package `python3-venv`
```
sudo apt update
sudo apt install python3-venv
```

## 5. Create a virtual environment: After installing the `python3-venv` package,
you can then create the virtual environment with the correct command:
```
screen -S gaiabot
```
```
python3 -m venv venv
```
This will create a `venv` folder in your current directory.

## 6. Activate the virtual environment: Once the virtual environment is created, you need to activate it:
```
source venv/bin/activate
```
This will change your shell prompt to indicate that the virtual environment is active.

## 7. Install any dependencies (if needed): Once the virtual environment is activated,
you can install your Python dependencies using `pip`
```
pip install -r requirements.txt
```
## 8. Open the `account.txt` file with `nano`
```
nano account.txt
```
Add the API key and API URL to the file:

- On the first line, put the API Key. [https://www.gaianet.ai/setting](https://www.gaianet.ai/setting/gaia-api-keys)
- On the second line, put the API URL. go to `https://your node id.us.gaianet.network`
- Click on `API Tutorial` in the bottom corner of the Go to Chat screen.
- Copy `https://llama.gaia.domains/v1/chat/completions`
- Copy the API key and replace it in `account.txt`

## 9. Open `message.txt`
```
nano message.txt
```
Add messages that you want to be used in your bot.
These could be predefined prompts or anything you want the bot
to send. Each message should be on a separate line.

[For example:](https://github.com/CryptoAirdropHindi/Gaianet-BOT/blob/main/message)
Save the file:

After adding your messages, press `Ctrl + X` to exit.
Press `Y` to confirm saving the changes.
Press `Enter` to save the file with the current name (`message.txt`).

## 10. node run
```
python3 bot.py
```

## stop the Node
```
docker stop gaianet && docker rm gaianet && Gaianet-BOT
```

---
"Great, all set! If you have any questions, don’t hesitate to ask in our Telegram channel."
Or if you'd like something more friendly and engaging:
- Telegram - https://t.me/Crypto_airdropHM
- Youtube - https://www.youtube.com/@CryptoAirdropHindi6
