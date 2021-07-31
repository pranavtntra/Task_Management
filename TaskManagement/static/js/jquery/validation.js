$(document).ready(function() {
    $("#signupform").validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            username: {
                required: true,
                minlength: 5,
            },
            firstName: {
                required: true,
                minlength: 2,
            },
            lastName: {
                required: true,
                minlength: 2,
            },
            contact: {
                required: true,
            },
            password1: {
                required: true,
                minlength: 8
            },
            password2: {
                equalTo: "#id_password1"
            }
        },
        messages: {
            email: {
                required: "This field is required.",
                email: "Please enter a valid email address.",
            },
            username: {
                required: 'Enter your username!',
                minlength: 'Enter more than two character!',
            },
            firstName: {
                required: 'Enter your name!',
                minlength: 'Enter more than two character!',
            },
            lastName: {
                required: 'Enter your name!',
                minlength: 'Enter more than two character!',
            },
            contact: {
                required: 'Enter your Number!',
            },
            password1: {
                required: "Please provide a password",
                minlength: "Your password must be at least 8 characters long"
            },
            password2: {
                equalTo: "Please enter the same password as above"
            }
        }
    });
    $("#loginform").validate({
        rules: {
            login: {
                required: true,
            },
            password: {
                required: true,
            }
        },
        messages: {
            login: {
                required: "Enter your email address"
            },
            password: {
                required: "Enter your valid password"
            }

        }
    });
    $("#add_task").validate({
        rules: {
            title: {
                required: true,
                minlength: 5,
            },
            description: {
                required: true,
                minlength: 10,
            }
        },
        messages: {
            title: {
                required: "Enter valid task name"
            },
            description: {
                required: "Enter proper description"
            }

        }

    });
    $("#add_subtask").validate({
        rules: {
            title: {
                required: true,
                minlength: 5,
            },
            description: {
                required: true,
                minlength: 10,
            }
        },
        messages: {
            title: {
                required: "Enter valid task name"
            },
            description: {
                required: "Enter proper description"
            }

        }

    });

});