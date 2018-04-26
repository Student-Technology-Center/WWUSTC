$(document).ready(function() {
	$('input[type=text]').parent().addClass('ui input');
	$('input[type=email]').parent().addClass('ui input');
	$('input[type=password]').parent().addClass('ui input');
});

function handleLogin() {
	$.ajax({
		type: "POST",
		url: "/user/api/user_login/",
		data: $('#login_form form').serialize(),
		success: function(data) {
			if (data.failed) {
				errs = $('#errors')
				errs.empty();
				var keys = Object.keys(data.failed);

				for (var i = 0; i < keys.length; i++) {
					errs.append("<h3 style='color: red;'> " + 
						toTitleCase(keys[i]) + ": " + data.failed[keys[i]] + "</h3>")
				}
			} else {
				window.location = '/';
			}
		}
	});

	return false;
}

function handleRegistration() {
	$.ajax({
		type: "POST",
		url: "/user/api/register/",
		data: $('#register_form form').serialize(),
		success: function(data) {
			if (data.failed) {
				errs = $('#errors')
				errs.empty();
				var keys = Object.keys(data.failed);

				for (var i = 0; i < keys.length; i++) {
					errs.append("<h3 style='color: red;'> " + 
						toTitleCase(keys[i]) + ": " + data.failed[keys[i]] + "</h3>")
				}
			} else {
				window.location = '/';
			}
		}
	});

	return false;
}

var register = false;
var login = true;

function setRegister(el) {
	if (register)
		return

	register = true;
	login = false;

	$(el).toggleClass('active');
	$('#login-btn').toggleClass('active');
	$('#login_form').css('visibility', 'hidden');
	$('#register_form').css('visibility', 'visible');
}

function setLogin(el) {
	if (login)
		return;

	register = false;
	login = true;

	$(el).toggleClass('active');
	$('#register-btn').toggleClass('active');
	$('#register_form').css('visibility', 'hidden');
	$('#login_form').css('visibility', 'visible');
}

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){
    	return txt.charAt(0).toUpperCase() + 
    		txt.substr(1).toLowerCase();});
}
