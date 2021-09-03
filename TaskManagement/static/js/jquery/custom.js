// ======for searchig or pagination in userlist page======
$(document).ready(function() {
const searchInput = document.getElementById('search_here')
console.log(searchInput)

const searchdata =(search_here) => {
  if (search_here.length > 2 || search_here.length < 1){
    var page = 1
    userListAjax(search_here, page)
    return false
  }
}

searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value);
    searchdata(e.target.value);
    
})

$(".pagination-ajax").click(function(e){
  e.preventDefault();
  if ($('#search_here').val() != "")
    search_here = $('#search_here').val();
  else
    search_here = ""
  page = $(this).attr('page');
  console.log('search'+search_here+'page'+page)
  if (search_here.length > 2 || search_here.length < 1){
    userListAjax(search_here, page)
    return false
  }
  });
});

function userListAjax(search, page){
  var url= $('#search_here').attr('url')
  $.ajax({
    type: "GET",
    url: url,
    data: {
        'page': page,
        'search': search,
    },
    success: function(data){
        $('#search_result').html(data)
    },
    error: function(data) {
        console.log("error")
    }
  }); 
}


// =======pop-up for delete user in userlist=======
$.ajax('{% url "deleteuser" details.id %}', {
  method: 'POST',
  success: function() {
      window.location.reload();
  },
});



// =====sorting the user details table by username and user first_name=====
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("btable");
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
            shouldSwitch= true;
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
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }