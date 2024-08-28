import os
import time
from datetime import datetime

# Set the IP address you want to ping
IP_ADDRESS = "8.8.8.8"

# Set the log file name
LOG_FILE = "ping_log-8.8.8.8.txt"

def log_message(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")

while True:
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ping the IP address
    response = os.system(f"ping -n 1 {IP_ADDRESS}")

    # Check the response and log the result
    if response == 0:
        log_message(f"{timestamp} Ping OK")
    else:
        log_message(f"{timestamp} Ping ERROR")

    # Wait for 1 second before the next ping
    time.sleep(1)