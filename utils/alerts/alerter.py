import smtplib
from email.mime.text import MIMEText
from django.conf import settings

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
    "uscell":"email.uscc.net"
}

def text(phone_num, carrier, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    print("Sending text \nfrom: {} \nto: {} \nsaying: {}.".format(EMAIL_USERNAME, "{}@{}".format(phone_num, carriers[carrier]), msg))
    server.sendmail(EMAIL_USERNAME, "{}@{}".format(phone_num, carriers[carrier]), msg)

def email(email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com:587')

    msg = MIMEText(message)
    msg['From'] = EMAIL_USERNAME
    msg['To'] = email
    msg['Subject'] = subject

    server.ehlo()
    server.starttls()

    try:
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except:
        print("Email couldn't be sent. Probably Googles server's rejecting login request.")
