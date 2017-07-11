import smtplib

from texter_logins import USERNAME, PASSWORD

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

def email(email, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, email, msg)

if __name__ == "__main__":
    text("4256985465", "verizon", "Hey this is a test to see if I can send longer texts and/or emails. Idk if this helps.")
