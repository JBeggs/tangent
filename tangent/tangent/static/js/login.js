// Well don't we just love javascript

$(".user").focusin(function(){$(".inputUserIcon").css("color", "#e74c3c");}).focusout(function(){$(".inputUserIcon").css("color", "white");});
$(".pass").focusin(function(){$(".inputPassIcon").css("color", "#e74c3c");}).focusout(function(){ $(".inputPassIcon").css("color", "white");});


// These functions are in reverse order
// login is the last to run
// This hack isn't working, login of user not working
function login(data){
    $.ajax({
        url: '/login_user/',
        type: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        data:JSON.stringify(data),
        success: function(return_data) { 
                    $("#login_error").html("lOGGIN IN...");
                    window.location = return_data.url;},
        error : function(){$("#login_error").html("Please Try me again...");}
    });
};





function token() {

    $.ajax({
            url: 'http://staging.tangent.tngnt.co/api-token-auth/',
            type: 'POST',
            data: {"username":"pravin.gordhan","password":"pravin.gordhan",}, 
            success: function(data) {
                remote_link(data.token)
                },
            error : function(){$(".alert p").html("Error importing data");}
        })


};


function remote_link(token){


    data = '';
    api_calls = [
        'http://staging.tangent.tngnt.co/api/employee/','http://staging.tangent.tngnt.co/api/group/',
        'http://staging.tangent.tngnt.co/api/review/','http://staging.tangent.tngnt.co/api/leave/',
        "http://staging.tangent.tngnt.co/api/public-holidays/","http://staging.tangent.tngnt.co/api/customer/"];

    for (i = 0; i < api_calls.length; i++) {    

        $.ajax({
            url: api_calls[i],
            type: 'GET',
            dataType: 'json',
            contentType: 'application/json',
            headers: {'Authorization': "Token " + token,},
            success: function(data) {

                    $.ajax({
                        url: '/import_employees/',
                        type: 'POST',
                        dataType: 'json',
                        contentType: 'application/json',
                        data:JSON.stringify(data),
                        success: function(return_data) 
                                    {
                                        $(".alert p").html("Waiting for next import...");

                                    },
                        error : function(){$(".alert p").html("Please Try me again...");}
                    });

            },
            error : function(){$("#login_error").html("Please Try me again...");}
        });
    } 

}

//
$(".profile").click(function() {
    $.ajax({
        url: '/profile/',
        type: 'GET',
        data: {"keyword":""}, 
        success: function(data) {
           $("#employee_stats").html(data);
        },
        error : function(){}
    });

});

$(".form-control").keypress(function(keyword) {
    $search = $("#search_control").val();
    if($search!=""){
        $.ajax({
            url: '/search/',
            type: 'POST',
            data: {"keyword":$search}, 
            success: function(data) {

               $("#employee_stats").html(data);

            },
            error : function(){}
        });
    }
});

//Initial login request using token and username & password
// on success send token with function get_employees...
//$("#login_form" ).submit(function( event ) {
//    $("#login_error").html("Please Wait...  ");
//    $.ajax({
//        url: 'http://staging.tangent.tngnt.co/api-token-auth/',
//        type: 'POST',
//        data: $('#login_form').serialize(), 
//        success: function(data) {get_employees(data.token);},
//        error : function(){$("#login_error").html("Invalid username or password");}
//    });
//  event.preventDefault();
//});
