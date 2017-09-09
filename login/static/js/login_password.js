$(document).ready(function() {
    $('#reset').click(function() {
        var username = $('#username').val();
        if (username === "") {
            $('#reset-warning').html('Please enter a valid username (in the username box)')
        } else {
            $.ajax({
                url: '/user/api/send_user_email/',
                data: { user:username }
            })
        }
    })
})