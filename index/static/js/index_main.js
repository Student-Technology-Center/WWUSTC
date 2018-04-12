$(document).ready(function() {

    getTodaysShifts();
});

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