(function($) {
    $.fn.countdown = function(options, callback) {

        //custom 'this' selector
        thisEl = $(this);

        //array of custom settings
        var settings = { 
            'date': null,
            'format': null
        };

        //append the settings array to options
        if(options) {
            $.extend(settings, options);
        }
        
        //main countdown function
        function countdown_proc() {
            
            eventDate = Date.parse(settings['date']) / 1000;
            currentDate = Math.floor($.now() / 1000);
            
            if(eventDate <= currentDate) {
                callback.call(this);
                clearInterval(interval);
            }
            const now = new Date();
            
            hours = now.getHours();
            minutes = now.getMinutes();
            seconds=now.getSeconds();
            
            
            //update the countdown's html values.
            if(!isNaN(eventDate)) {
                thisEl.find(".days").text(days);
                thisEl.find(".hours").text(hours);
                thisEl.find(".minutes").text(minutes);
                thisEl.find(".seconds").text(seconds);
            } else { 
                alert("Invalid date. Here's an example: 12 Tuesday 2012 17:30:00");
                clearInterval(interval); 
            }
        }
        
        //run the function
        countdown_proc();
        
        //loop the function
        interval = setInterval(countdown_proc, 1000);
        
    }
}) (jQuery);