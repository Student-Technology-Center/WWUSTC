import smtplib
from email.mime.text import MIMEText

from utils.alerts.texter_logins import USERNAME, PASSWORD

carriers = {
    "at&t":"txt.att.net",
    "tmobile":"tmomail.net",
    "verizon":"vtext.com",
    "sprint":"page.nextel.com",
    "boost":"myboostmobile.com",
    "cricket":"mms.cricketwireless.net",
    "alltell":"message.alltel.com",
    "metroPCS":"mymetropcs.com",
    "projectFi":"msg.fi.google.com",
}

def text(phone_num, carrier, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    print("Sending text \nfrom: {} \nto: {} \nsaying: {}.".format(USERNAME, "{}@{}".format(phone_num, carriers[carrier]), msg))
    server.sendmail(USERNAME, "{}@{}".format(phone_num, carriers[carrier]), msg)

def email(email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com:587')

    msg = MIMEText(message)
    msg['From'] = USERNAME
    msg['To'] = email
    msg['Subject'] = subject

    server.ehlo()
    server.starttls()

    try:
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        print("Email couldn't be sent. Probably Googles server's rejecting login request.")