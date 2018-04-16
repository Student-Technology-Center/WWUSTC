from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponse

def user_is_email_confirmed(function):
	def wrap(request, *args, **kwargs):
		if request.user.userhiddenattributes.confirmed_account:
			return function(request, *args, **kwargs)
		else:
			return redirect('/user/email/')

	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap