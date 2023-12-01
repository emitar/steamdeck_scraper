# Steam Deck Refurbished Availability Checker

I couldn't find a tool that would allow me to check the availability of the Steam Deck Refurbished from the command line (CLI), so I decided to create something myself.

For this purpose, I used Python version 3.10.12.

Assuming you already have Python installed, below are the steps I took on Ubuntu 22.04 to run the script.

## Steps:

1. **Install Chrome:**
   ```bash
   wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
   sudo apt update 
   sudo apt install -f ./google-chrome-stable_current_amd64.deb 

2. **Install Python Packages:**
   ```bash
   pip install selenium webdriver-manager pytelegrambotapi

3. After downloading the code, simply substitute your Telegram bot data to receive notifications when the Steam Deck becomes available for purchase.

4. **Run script**
   ```bash
    python steam_deck_checker.py

5. **Add Script to CRON:**
  Add the script to your CRON tasks for periodic execution. For example, to run the script every 10 minutes:

   ```bash
    */10 * * * * /usr/bin/python3 /path/to/steam_deck_checker.py

Feel free to customize the script according to your needs.

If you encounter any issues or have suggestions for improvements, please let me know!



(I'm not programer)

