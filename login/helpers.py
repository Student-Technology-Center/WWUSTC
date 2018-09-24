from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from .models import UserHiddenAttributes
from utils.message import send_stc_email
from django.utils import timezone

def send_user_confirmation_email(request, user):
	url = request.get_raw_uri().replace(request.get_full_path(), "")
	key = user.userhiddenattributes.confirmation_key

	msg = """
			Please confirm your account for wwustc.com.

			You can either click this link: {}/user/email/{}

			Or you can enter the code below at {}/user/email/

			\t{}
		  """.format(url, key, url, key)

	send_stc_email("Confirm your account on WWUSTC.com", msg, [user.email], threaded=True)

def check_user_confirmation_key(key):
	user = None

	try:
		user = UserHiddenAttributes.objects.get(confirmation_key=key)
	except (ValueError, ValidationError) as e:
		return False

	user.confirmed_account = True
	user.save()
	return user.confirmed_account

def send_password_reset_email(request, user):
	url = request.get_raw_uri().replace(request.get_full_path(), "")
	key = UserHiddenAttributes.objects.get(user=user).reset_key

	msg = """
			You've requested to reset your wwustc.com password.
			This is a one time use key that will expire in one hour.

			Click this link to do so: {}/user/reset/{}

			Or you can enter the code below at {}/user/reset/

			\t{}
		  """.format(url, key, url, key)

	send_stc_email("WWUSTC.com password reset notice", msg, [user.email], threaded=True)


def check_password_reset_token(key):
	user_attributes = UserHiddenAttributes.objects.filter(reset_key=key)

	if not user_attributes.count() == 1:
		return False

	reset_timeout = timezone.now() - user_attributes.first().reset_request_time

	if reset_timeout.seconds < 3600:
		return True
	else:
		return False
