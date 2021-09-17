$("#id_project").change(function() {
    var project_id = $(this).val();
    $.ajax({
        url: $("#add_subtask").attr("data-url"),
        method: 'get',
        data: {
            'project_id': project_id
        },
        success: function(data) {
            console.log(data)
            $('#id_parent_task').html("<option>select</option>");
            data.forEach(function(e) {
                op = $('<option value ="' + e.id + '">' + e.title + '</option>');
                $('#id_parent_task').append(op);
            });
        }
    });

});