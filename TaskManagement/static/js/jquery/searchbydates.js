$('#search').click(function() {
    var start_date = $("#start_date").val();
    var end_date = $("#end_date").val();
    const p_id = document.getElementById('project_tasklist').value

    $.ajax({

        url: $("#search").data('url'),
        method: 'get',
        data: {
            'id': p_id,
            'start_date': start_date,
            'end_date': end_date,
        },
        success: function(data) {
            $("#search-results").empty();
            console.log("yooooooo")
            $('#search_result').html(data);

        },
        error: function(data) {
            console.log("error");
        }
    });
});