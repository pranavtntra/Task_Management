$('#project_sprintlist').change(function() {
    var id = $(this).val();
    console.log(id);

    $.ajax({
        url: $(this).data('url'),
        method: 'get',
        data: {
            'id': id,
        },
        success: function(data) {
             console.log("SUCCESS");
             console.log(data);
            $("#search-results").empty();

            JSON.parse(data["sprints"]).forEach((item) => {
                console.log(item)

            });
        },
        error: function(data) {
            console.log("error");
            console.log(data)
        }
    });
});