var currentInfo;

//num is the limit.
function getRandomWholeNumber(num) {
    return Math.ceil(Math.random() * num)
}

var rotation_cap = 360;
var movement_cap = 300;
var scale_cap = 2;

$(document).ready(function() {
    $('.app_button').mouseenter(function() {
        currentInfo = $(this).children()[0].children[2].innerHTML;
        $('#app_info').text(currentInfo);
    })
    $( window ).konami({
		cheat: function() {
			$('.app_link').each(function (i, obj){
                $(this).css({
                    "background-color": randRGB(),
                }, 1000);

                var rotationAmt = getRandomWholeNumber(rotation_cap).toString() + "deg";
                var moveAmt = getRandomWholeNumber(movement_cap).toString() + "px";
                var scaleAmt = getRandomWholeNumber(scale_cap).toString();

                $(this).parent().css({
                    "transform": "rotate(" + rotationAmt + ") translateX(" + moveAmt + ") translateY(" + moveAmt + ") scale(" + scaleAmt + ")"
                }, 1000);
            });
		}
	});

    getTodaysShifts();
});

function getTodaysShifts() {

    var today = moment().format('YYYY-MM-DD')
    var time = moment().format('HH:mm')

    console.log(time)

    $.ajax({
        url: '/shifts/api/get_shifts/?start=' + today + '&end=' + today,
        fail: function () {
            setError("Something went wrong - file a bug report. Please retry the submission");
        },
        success: function(data) {
            data.success.forEach(function(e) {
                console.log(e)
            })
        }
    })

}