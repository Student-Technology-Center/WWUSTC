/* Don't make the quotes longer than the 'after 9pm' one, it'll mess up the html */
quotes = [
    'Can I get a laptop?',
    'Do you have any appointments after 9PM?', // <---- No longer than this quote.
    'Do you have any appointments before 8AM?',
    "I'd like to schedule a 1 on 1.",
    'The printers are down.',
    'Wheres the black and white printer?',
    'Where is Haggard Hall?',
    'Do you have any laptops?',
    'Do you have a paperclip?',
    'Whoa are those 3d printers?',
    'These quotes kind of suck.',
    '12345 is a bad password!',
    'SOPA means LOSER in Swedish!',
    'Can Paul help with my PHP?',
    'No one showed up to my workshop.',
    '**Steals scissors**',
    'Do you guys have a rubberband?',
    'What is the VR room?',
    "Yeah I've tried every way of printing.", // <---- Or this one.
    'Can you find all the easter eggs?',
    'Does anyone know Wordpress?',
    'Where are we grabbing from?',
    'Please submit your timesheets.',
    'Go talk to Circulation Desk.',
    'Is Zoes open?',
    'Hi.',
    "tHerE's ToO mANy mEmEs aT tHE sTc."
]

quote_choice = quotes[Math.floor((Math.random() * quotes.length))];

$(document).ready(function() {
    $('#login h2').delay(700).animate({
        opacity:'0',
    }, 1000, function(){
        $(this).text(quote_choice).animate({
            opacity:'1',
        }, 1000);
    })

    $('#welcome').delay(1500).animate({
        opacity:'0',
    }, 1000, function(){
        $(this).text(quote_choice).animate({
            opacity:'1',
        }, 1000);
    })
})
