//Hook up the tweet display

$(document).ready(function() {
                           
    $(".countdown").countdown({
                date: "28 August 2023 13:38:00",
                format: "on"
            },
            
            function() {
                // callback function
            });

}); 