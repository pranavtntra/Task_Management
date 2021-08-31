$(".add").click(function () {
  var proj = $(this).val();
    $.ajax({
        url: $("#add").data('url'),
        type: 'get',
        data: {
          'proj': proj
        },
        datatype: 'json',
        beforeSend: function () {
            $("#modal-add").modal("show");
          },
          success: function (data) {
            $("#modal-add .modal-content").html(data.form);
          },
        error: function(data) {
            console.log("error")
        }
    })}); 

    $("#modal-add").on("submit", ".add-member", function () {
      $("#modal-add").modal("hide");  
      var form = $(this);
      var dat = $(this).data("id");
      $.ajax({
        url: form.attr("action"),
        data: form.serialize() + "&" + "project" + "=" + dat,
        type: "POST",
        dataType: 'json',

        success: function (data) {
          if (data.form_is_valid) {
            alert("Member Added!");  
          }
          else {
            $("#modal-add .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });



// $(".view").click(function () {
//   var proj = $(this).val();
//   $.ajax({
//     url: $("#view").data('url'),
//             type: 'get',
//             data: {
//               'proj': proj
//             },
//             datatype: 'json',
//             beforeSend: function () {
//                 $("#modal-view").modal("show");
//               },
//               success: function (data) {
//                 $("#modal-view .modal-content").html(data.form);
//               },
//             error: function(data) {
//                 console.log("error")
//             }
//         })}); 