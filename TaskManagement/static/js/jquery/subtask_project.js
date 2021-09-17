$("#id_parent_task").change(function() {
    var task_id = $(this).val();
    $.ajax({
        url: $("#add_subtask").attr("data-url"),
        method: 'get',
        data: {
            'task_id': task_id
        },
        success: function(data) {
            $("#id_project").html(data);
        }
    });

});