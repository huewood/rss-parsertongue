import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.SENDER_EMAIL, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.SENDER_EMAIL,config.RECEIVER_EMAIL, message)
        server.quit()
        print("Success: Email sent.")
    except:
        print("Email failed to send.")

# Debug
#subject = "Test subject"
#msg = "Hello World!"

#send_email(subject, msg)