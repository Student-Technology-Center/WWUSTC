from django.core.mail import send_mail, get_connection
from django.conf import settings

from threading import Thread

def send_stc_email(subject, message, recipients, threaded=True):

    #This is now only required if on a live server.
    #You can use the console backend which will output emails to console if on dev.
    if (not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD) and not settings.DEBUG:
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

    #Selects where emails will go
    if settings.DEBUG:
        conn = get_connection('django.core.mail.backends.console.EmailBackend')
    else:
        conn = settings.EMAIL_BACKEND

    if not threaded or settings.DEBUG:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipients,
            connection=conn
        )
    else:
        email_t = Thread(
            target=send_mail,
            args=(subject, message, settings.EMAIL_HOST_USER, recipients)
        )
        email_t.start()

def send_stc_text(subject, message, recipients):
	pass
