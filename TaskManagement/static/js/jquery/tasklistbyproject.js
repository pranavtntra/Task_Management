statusDict = {
    '1': 'To-do',
    '2': 'In-progress',
    '3': 'Done',
    '4': 'Declined',
    '5': 'Ready For Testing',
    '6': 'Code Review',
    '7': 'Testing in-progress'
}
tasktypeDict = {
    '1': 'Bug',
    '2': 'Improvement',
    '3': 'New Feature',
    '4': 'Story',
    '5': 'Task',
    '6': 'Epic'
}
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
            $("#btable").empty();
            JSON.parse(data["task"]).forEach((item) => {
                console.log(item)

                var row = "<tr>" +
                    "<td>" + item.title + "</td>" +
                    "<td>" + item.assigned_to__first_name + "</td>" +
                    "<td>" + statusDict[item.status] + "</td>" +
                    "<td>" + item.priority + "</td>" +
                    "<td>" + statusDict[item.tasktype] + "</td>" +
                    "</tr>";
                $('#mytable').append(row);
            });
        },
        error: function(data) {
            console.log("error");
        }
    });
});