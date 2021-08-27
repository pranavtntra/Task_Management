const searchInput = document.getElementById('search_here')
const searchdata = (search_here) => {
    const p_id = document.getElementById('project_tasklist').value
    console.log(p_id);
    console.log(search_here);
    $.ajax({
        type: "GET",
        url: $("#search_here").data('url'),
        data: {
            'id': p_id,
            'search_here': search_here,
        },
        success: function(data) {
            // console.log(data)
            $("#search-results").empty();
            $('#search_result').html(data);
        },
        error: function(data) {
            console.log("error")
        }
    });
    return false
}
searchInput.addEventListener('keyup', e => {
    console.log(e.target.value);
    searchdata(e.target.value);
})