$(document).ready(function() {
	$('#login').click(() => {
		$('#register_form').css("visibility", "hidden");
		$('#register_form').css("display", "none");
		$('#login_form').css("visibility", "visible");
		$('#login_form').css("display", "block");
	});

	$('#register').click(() => {
		$('#login_form').css("visibility", "hidden");
		$('#login_form').css("display", "none");
		$('#register_form').css("visibility", "visible");
		$('#register_form').css("display", "block");
	});

	$('input[type="email"]').keypress((data) => {
		var input = $(this).val();
		console.log(input);
	})
});

function handleLogin() {
	$.ajax({
		type: "POST",
		url: "/user/api/user_login/",
		data: $('#login_form form').serialize(),
		success: function(data) {
			if (data.failed) {
				errs = $('#login_errors')
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
				errs = $('#register_errors')
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

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){
    	return txt.charAt(0).toUpperCase() + 
    		txt.substr(1).toLowerCase();});
}
