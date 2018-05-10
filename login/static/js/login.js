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
				writeErrors(Object.keys(data.failed), data)
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
				writeErrors(Object.keys(data.failed), data);
			} else {
				window.location = '/';
			}
		}
	});

	return false;
}

var login = true;

function flipItem() {
	login = !login;

	clearErrors();
	flipErrorDisplay(false);

	if (login) {
		$('#' + REGISTER_ID).css({'display': 'none'});
		$('#' + LOGIN_ID).css({'display':'block'});
	} else {
		$('#' + LOGIN_ID).css({'display': 'none'});
		$('#' + REGISTER_ID).css({'display':'block'});
	}
}

var errors = false;

function clearErrors() {
	$('#' + ERRORS_ID).empty();
}

function flipErrorDisplay(open) {
	errors = open;

	if (errors) {
		errs.parent().css("display", "block");
	} else {
		errs.parent().css("display", "none");
	}
}

function writeErrors(errors, data) {
	errs = $('#' + ERRORS_ID)

	flipErrorDisplay(true);
	clearErrors();

	for (var i = 0; i < errors.length; i++) {
		errs.append(getErrorMsg(toTitleCase(errors[i]), data.failed[errors[i]]));
	}
}

/* This block of code is why React exists */
function getErrorMsg(header, data) {
	var str = "<div class='ui negative message'> <div class='header'>"+header+"</div><p> "+data+"</p></div>";
	return str;
}

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){
    	return txt.charAt(0).toUpperCase() + 
    		txt.substr(1).toLowerCase();});
}
