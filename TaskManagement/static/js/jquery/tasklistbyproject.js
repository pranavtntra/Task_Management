$('#project_tasklist').change(function() {

    var id = $(this).val();
    console.log(id);

    $.ajax({
        url: $(this).data('url'),
        method: 'get',
        data: {
            'id': id,
        },
        success: function(data) {
            $("#search-results").empty();
            JSON.parse(data["task"]).forEach((item) => {
                console.log(item)

                var row = "<tr>" +
                    "<td>" + item.title + "</td>" +
                    "<td>" + item.assigned_to__first_name + "</td>" +
                    "<td>" + item.status + "</td>" +
                    "<td>" + item.priority + "</td>" +
                    "<td>" + item.tasktype + "</td>" +
                    "</tr>";
                $('#mytable').append(row);
            });
        },
        error: function(data) {
            console.log("error");
        }
    });
});