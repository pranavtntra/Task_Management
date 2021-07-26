
$(document).ready(function(){
    $("#signup_form").validate({
        rules: {
            email: {
                required: true,
                email: true,
                // accept:"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"           
            },
            username: {
                required: true,
                minlength: 2,
            },
            firstName: {
                required: true,
                minlength: 2,
                // lettersonly: true
            },
            lastName: {
                required: true,
                minlength: 2,
                // lettersonly: true
            },
            contact: {
                required: true,
            },
            password1 : {
                required: true,
                minlength : 8
            },
            password2 : {
                equalTo : "#id_password1"
            }
        },
        messages: {
            email: {
                required: "This field is required.",
                email: "Please enter a valid email address.",        
            },
            username: {
                required: 'Enter the username!',
                minlength: 'Enter more than two character!',
                // lettersonly: 'Enter valid name!!!'
            },
            firstName: {
                required: 'Enter the name!',
                minlength: 'Enter more than two character!',
                // lettersonly: 'Enter valid name!!!'
            },
            lastName: {
                required: 'Enter the name!',
                minlength: 'Enter more than two character!',
                // lettersonly: 'Enter valid name!!!'
            },
            contact: {
                required: 'Enter the Number!',
            },
            password1 : {
                required: "Please provide a password",
                minlength: "Your password must be at least 8 characters long"
            },
            password2: {
                equalTo: "Please enter the same password as above"
            }
        }
    });
});
