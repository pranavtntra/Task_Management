
const searchdata = () => {
    $.ajax({
        type: "GET",
        url: $("#search_here").data('url'),

        data: {
            'search': $("#search_here").val(),
            'start_date': $("#startdate").val(),
            "end_date": $("#enddate").val(),
            'sort': $('#sort').val(),
        },
        success: function(data){
            $('#search_result').html(data)
            $(".delete_content").remove();
        },
        error: function(data) {
            console.log("error")
          
        }

    });
    return false
}

document.getElementById('search_here').addEventListener('keyup', e=>{

    searchdata(); 
})

document.getElementById('sort').addEventListener('change', e=>{

    searchdata(); 
})

document.getElementById('search').addEventListener('click', e=>{

    searchdata(); 
})


