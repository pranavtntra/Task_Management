const searchInput = document.getElementById('search_here')
console.log(searchInput)


const searchdata = (search_here) => {
    $.ajax({
        type: "GET",
        url: $("#search_here").data('url'),
        data: {
            'search_here': search_here

        },
        success: function(data) {
            $("#search-results").empty();
            $('#search_result').html(data)
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