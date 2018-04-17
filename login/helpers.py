from django.core.mail import send_mail

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

	send_stc_email("Confirm your account on WWUSTC.com", msg, [user.email], override=True)

def check_user_confirmation_key(key):
	user = UserHiddenAttributes.objects.get(confirmation_key=key)
	user.confirmed_account = True
	user.save()
