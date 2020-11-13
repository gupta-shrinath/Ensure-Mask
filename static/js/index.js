// Login API Call //
$('#form-login').submit(function (e) {
    var form = $(this);
    var error = form.find(".error");
    var data = form.serialize();
    $.ajax({
        url: "/user/login/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (r) {
            window.location.href = '/user/dashboard/'
            console.log('Success' + r);
        },
        error: function (r) {
            error.text(r.responseJSON.error).removeClass("error--hidden");
            console.log('Failed', r);
        }
    });
    e.preventDefault();
});

// Register API Call //
$('#form-register').submit(function (e) {
    var form = $(this);
    var error = document.getElementById('registerError');
    var data = form.serialize();
    console.log(data)
    $.ajax({
        url: "/user/register/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (r) {
            console.log('Registration Sucess', r);
        },
        error: function (r) {
            console.log('Registration Fail', r);
            error.innerText = r.responseJSON.error;
            error.removeClass('error--hidden');
        }
    });
    e.preventDefault();
});