$(document).ready(function() {
    $("#signupform").validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            username: {
                required: true,
                minlength: 2,
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
    $("#user_signup_form").validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            username: {
                required: true,
                minlength: 2,
            },
            first_name: {
                required: true,
                minlength: 2,
            },
            last_name: {
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
            first_name: {
                required: 'Enter your name!',
                minlength: 'Enter more than two character!',
            },
            last_name: {
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
    $("#updateform").validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            username: {
                required: true,
                minlength: 2,
            },
            first_name: {
                required: true,
                minlength: 2,
            },
            last_name: {
                required: true,
                minlength: 2,
            },
            contact: {
                required: true,
            },
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
            first_name: {
                required: 'Enter your First name!',
                minlength: 'Enter more than two character!',
            },
            last_name: {
                required: 'Enter your Last name!',
                minlength: 'Enter more than two character!',
            },
            contact: {
                required: 'Enter your Number!',
            },
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
    $("#changepassword").validate({
        rules: {
            old_password: {
                required: true,
            },
            new_password1: {
                required: true,
                minlength: 8
            },
            new_password2: {
                equalTo: "#id_new_password1"
            },
        messages: {
            old_password: {
                required: "This field is required.",
            },
            new_password1: {
                required: "This field is required.",
                minlength: "Your password must be at least 8 characters long"
            },
            new_password2: {
                equalTo: "Please enter the same password as above"
            }
        }
        },
    })

});