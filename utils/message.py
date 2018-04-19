from django.core.mail import send_mail
from django.conf import settings

from threading import Thread

def send_stc_email(subject, message, recipients, override=False, threaded=True):
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        print(
            """
You have not set one of the following environment variables:

EMAIL_USERNAME
EMAIL_PASSWORD

Please set these to a proper gmail account, otherwise
email will fail. If this is on a production server
ask for the WWU STC gmail username and password and set it
in the webservers configuration.

If you're still confused, talk to Christian or Alex.
            """
        )
        return

    if not settings.DEBUG or override:
        if not threaded:
            send_mail(
                subject,
	        message,
	        settings.EMAIL_HOST_USER,
	        recipients
	    )
        else:
            email_t = Thread(
                target=send_mail,
                args=(subject, message, settings.EMAIL_HOST_USER, recipients)
            )
            email_t.start()

def send_stc_text(subject, message, recipients):
	pass
