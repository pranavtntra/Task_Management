$('.technologies > li').each( function() {
    $(this).after('<input type="text" name="topic" required id="id_topic" disabled="disabled" >');
});
$('input[type="checkbox"]').click( function() {
    if($(this).is(':checked')){
        $(this).parent().parent().next().removeAttr("disabled");
    }
    else{
        $(this).parent().parent().next().attr("disabled","disabled");
    }
});