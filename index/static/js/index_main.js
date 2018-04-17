function logoutUser() {
   $.ajax({
        type: "GET",
        url: "/user/api/user_logout/",
        data: $('#login_form form').serialize(),
        success: function(data) {
            if (data.success)
                window.location = "/user/"
        }
    });
}