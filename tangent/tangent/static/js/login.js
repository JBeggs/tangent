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
// Tail end of importing reviews
function import_review(data){
    $.ajax({
        url: '/import_review/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data:JSON.stringify(data),
        success: function(return_data) 
                    {$("#login_error").html("Waiting for last import...");
                    login($('#username').val());},
        error : function(){$("#login_error").html("Please Try me again...");}
    });
};
// Basic importing reviews
function get_review(token){
    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api/review/',
        type: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: {'Authorization': "Token " + token,},
        success: function(data) {import_review(data);},
        error : function(){$("#login_error").html("Please Try me again...");}
    });
};
// Request to Django to import the employees
function import_employees(data,token){
    $.ajax({
        url: '/import_employees/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data:JSON.stringify(data),
        success: function(return_data) {
                    get_review(token);
                    $("#login_error").html("Waiting for imports...");},
        error : function(){ $("#login_error").html("Please Try me again...");}
    });
};
// Request to web API to get the employees data
function get_employees(token){
    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api/employee/',
        type: 'GET',
        dataType: 'json',
        contentType: 'application/json',
        headers: {'Authorization': "Token " + token,},
        success: function(data) {import_employees(data,token);},
        error : function(){$("#login_error").html("Please Try me again...");}
    });
};
//
function remote_link(){
    $.ajax({
        url: 'http://staging.tangent.tngnt.co/api-token-auth/',
        type: 'POST',
        data: {"username":"pravin.gordhan","password":"pravin.gordhan",}, 
        success: function(data) {get_employees(data.token);},
        error : function(){alert('frrrt');$("#login_error").html("Invalid username or password");}
    });
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
