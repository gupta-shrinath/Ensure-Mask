$('#photoOneImg').on('click', function () {
    $('#photoOne').trigger('click');
    $('#photoOne').change(function (e) {
        let fileName = e.target.files[0].name;
        $("#photoOneLabel").text(fileName);
        if (e.target.files && e.target.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#photoOneImg')
                    .attr('src', e.target.result)
                    .height(158)
            };
            reader.readAsDataURL(e.target.files[0]);
        }
    })
});

$('#photoTwoImg').on('click', function () {
    $('#photoTwo').trigger('click');
    $('#photoTwo').change(function (e) {
        let fileName = e.target.files[0].name;
        $("#photoTwoLabel").text(fileName);
        if (e.target.files && e.target.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#photoTwoImg')
                    .attr('src', e.target.result)
                    .height(158)
            };
            reader.readAsDataURL(e.target.files[0]);
        }
    })
});

$('#photoThreeImg').on('click', function () {
    $('#photoThree').trigger('click');
    $('#photoThree').change(function (e) {
        let fileName = e.target.files[0].name;
        $("#photoThreeLabel").text(fileName);
        if (e.target.files && e.target.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#photoThreeImg')
                    .attr('src', e.target.result)
                    .height(158)
            };
            reader.readAsDataURL(e.target.files[0]);
        }
    })
});

