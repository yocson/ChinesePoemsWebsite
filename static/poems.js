/**
 * Created by KSH on 16/8/27.
 */
$(document).ready(function () {
    $.getJSON("static/poems.json",function(result){
        $.each(result, function(i, data){
            $(".list-group").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +"-"+data.author+"</a>");
        });
    });
});



