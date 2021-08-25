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
                    "<td><span class='tag tag-info'>" + item.status + "</span></td>" +
                    "<td>" + item.priority + "</td>" +
                    "<td>" + item.tasktype + "</td>" + "<td>" + item.start_date + " to " +
                    item.end_date + "</td>" +
                    "</tr>";
                $('#mytable').append(row);
            });
        },
        error: function(data) {
            console.log("error");
        }
    });
});

// $('#search').click(function() {

//     var start_date = $(this).val();
//     console.log(start_date);

//     $.ajax({
//         url: $(this).data('url'),
//         method: 'get',
//         data: {
//             'start_date': start_date,
//         },
//         success: function(data) {
//             console.log('hello');

//         },
//         error: function(data) {
//             console.log("error");
//         }
//     });
// });

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("mytable");
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}