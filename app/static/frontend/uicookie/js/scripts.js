jQuery(function ($) {

    'use strict';

    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------

    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());

    $(document).bind("contextmenu",function(e) {
        e.preventDefault();
    });


    $("#contactForm").submit(function(){
        var email = $('#InputEmail').val();
        var name = $('#InputName').val();

        if ((email == '' || name == '' || email == undefined || name == undefined)) {
            alert("Please enter required field");
            return false;
        } else {
            $.ajax({
                url: '/contactus',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }

    })



}); // JQuery end


