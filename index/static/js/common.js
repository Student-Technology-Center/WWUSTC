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

function ajax_get(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'GET',
		success	: success
	})
}

function ajax_post(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'POST',
		success	: success,
		headers: {
			'X-CSRFToken' : getCookie('csrftoken')
		}
	})
}

function ajax_put(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'PUT',
		success	: success,
		headers: {
			'X-CSRFToken' : getCookie('csrftoken')
		}
	})
}

function ajax_delete(url, data, success) {
	$.ajax({
		url		: url,
		data	: data,
		type	: 'DELETE',
		success	: success,
		headers: {
			'X-CSRFToken' : getCookie('csrftoken')
		}
	})
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}