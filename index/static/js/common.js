function logoutUser(redirectURL) {
	$.ajax({
		method: 'GET',
		url: '/user/api/user_logout',
		success: function(data) {
			if (data.success) {
				window.location = redirectURL;
			} else {
				return false
			}
		}
	})
}

function getTodaysDate() {
	var date = new Date();
	return (date.getMonth() + 1) + '-' + date.getDate() + '-' + date.getFullYear();
}

function z(url, data) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'POST',
		headers	: { 'methodoverride' : 'DELETE' }
	})
}

function ajax_post(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'POST',
		success	: success
	})
}

function ajax_get(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'GET',
		success	: success
	})
}

/* Override the POST type with PUT */
function ajax_put(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'POST', //This is intentional.
		success	: success,
		headers	: { 'methodoverride' : 'PUT' }
	})
}

/* Override the POST type with DELETE */
function ajax_delete(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'POST',
		success	: success,
		headers	: { 'methodoverride': 'DELETE' }
	})
}