var currentInfo;

$(document).ready(function() {
    $('.app_button').mouseenter(function() {
        currentInfo = $(this).children()[0].children[2].innerHTML;
        $('#app_info').text(currentInfo);
    })
});