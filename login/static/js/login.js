var LOGIN_ID 		= 'login_form';
var REGISTER_ID 	= 'register_form';
var ERRORS_ID		= 'errors';

function handleLogin() {
	$.ajax({
		type: "POST",
		url: "/user/api/user_login/",
		data: $('#' + LOGIN_ID).serialize(),
		success: function(data) {
			if (data.failed) {
				writeErrors(Object.keys(data.failed))
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
		data: $('#' + REGISTER_ID).serialize(),
		success: function(data) {
			if (data.failed) {
				writeErrors(Object.keys(data.failed));
			} else {
				window.location = '/';
			}
		}
	});

	return false;
}

var login 		= true;

function flipItem() {
	login = !login;

	if (login) {
		$('#' + REGISTER_ID).css({'display': 'none'});
		$('#' + LOGIN_ID).css({'display':'visible'});
	} else {
		$('#' + LOGIN_ID).css({'display': 'none'});
		$('#' + REGISTER_ID).css({'display':'visible'});
	}
}

function writeErrors(errors) {
	errs = $('#' + ERRORS_ID)
	errs.empty();

	for (var i = 0; i < errors.length; i++) {
		errs.append(getErrorMsg(toTitleCase(errors[i]), data.failed[errors[i]]));
	}
}

/* This block of could is why react exists */
function getErrorMsg(header, data) {
	var str = "<div class='ui negative message'> \
				  <div class='header'> \
				    " + header + " \
				  </div> \
				  	<p> " + data + "</p> \
			   </div>";

	return str;
}

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){
    	return txt.charAt(0).toUpperCase() + 
    		txt.substr(1).toLowerCase();});
}
