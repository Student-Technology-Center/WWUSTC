from django.core.mail import send_mail
from django.conf import settings

def send_stc_email(subject, message, recipients, override=False):
	if not settings.DEBUG or override:
		send_mail(
			subject,
			message,
			settings.EMAIL_HOST,
			recipients
		)

def send_stc_text(subject, message, recipients):
	pass