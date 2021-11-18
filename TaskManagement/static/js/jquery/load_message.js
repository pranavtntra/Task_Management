$("#id_assigned_to").change(function() {
    var assigned_to = $(this).val();
    console.log(assigned_to);

    $.ajax({
        url: $("#add_task").attr("data-url"),
        method: 'get',
        data: {
            'assigned_to': assigned_to
        },
        success: function(data) {
            var name = $("#id_assigned_to option:selected").text();
            $("p").empty();

            var btn = document.createElement("p");
            btn.innerHTML = name + " have " + data + " tasks.";
            $("#id_assigned_to").after(btn);
        }
    });

});