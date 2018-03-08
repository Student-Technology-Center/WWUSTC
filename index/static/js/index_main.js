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
    var shifts = [];

    $.ajax({
        url: '/shifts/api/get_shifts/?start=' + today + '&end=' + today,
        fail: function () {
            console.log("Couldn't get shifts.")
        },
        success: function(data) {
            data.success.forEach(function(e) {
                var user = {}
                
                user.time = moment(e.datetime)
                user.name = e.name;
                user.up = e.up_for_grabs;

                shifts.push(user);
            })

            combineShifts(shifts)
        }
    })
}

function combineShifts(shifts) {

    var combined_shifts = [];

    shifts.forEach(function (shift) {
        var end = new moment(shift.time);
        end.add(1, 'hours');
        var shift_pool = [];

        shifts.forEach(function (nextShift) {

            if (nextShift.time.format('h:mm a') === end.format('h:mm a') && 
                nextShift.name === shift.name) {
                end.add(1, 'hours');
                shift_pool.push(nextShift);
            }
        })

        if (shift_pool.length >= 0) {
            combined_shifts.push(shift_pool);
        }
    })

    console.log(combined_shifts);

}