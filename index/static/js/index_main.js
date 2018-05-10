$(document).ready(function() {
	getThisHoursShifts();
})

function getThisHoursShifts() {
	var today = getTodaysDate();

	$.ajax({
		method: 'GET',
		url: '/shifts/api/get_shifts/',
		data: {
			'start': today,
			'end': today
		},
		success: function(data) {
			console.log(data)
		}
	})
}