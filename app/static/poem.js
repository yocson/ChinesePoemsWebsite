$(document).ready(function () {
    alert("ok");
    $.getJSON("static/poems.json",function(result){
        $.each(result, function(i, data){

        });
    });
});