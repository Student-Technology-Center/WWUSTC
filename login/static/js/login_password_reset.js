$(document).ready(function() {
    $('#reset').click(function() {
        var username = $('#username').val();
        $.ajax({
            url: '/user/api/send_user_email',
            data: { user:username }
        })
    })
})