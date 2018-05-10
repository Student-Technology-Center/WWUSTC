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