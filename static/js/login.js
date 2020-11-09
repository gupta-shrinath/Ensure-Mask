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