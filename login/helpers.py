from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from .models import UserHiddenAttributes
from utils.message import send_stc_email

def send_user_confirmation_email(request, user):
	url = request.get_raw_uri().replace(request.get_full_path(), "")
	key = user.userhiddenattributes.confirmation_key

	msg = """
			Please confirm your account for wwustc.com.

			You can either click this link: {}/user/email/{}

			Or you can enter the code below at {}/user/email/

			{}
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
