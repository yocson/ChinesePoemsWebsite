/**
 * Created by KSH on 16/8/27.
 */
$(document).ready(function () {
    $.getJSON("static/poems.json",function(result){
        $.each(result, function(i, data){
            if (data.cat == '五言绝句')
                $("#wyjj").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else if (data.cat == '七言绝句')
                $("#qyjj").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else if (data.cat == '五言律诗')
                $("#wyls").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else if (data.cat == '七言律诗')
                $("#qyls").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else if (data.cat == '五言古诗')
                $("#wygs").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else if (data.cat == '七言古诗')
                $("#qygs").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
            else
                $("#yf").append("<a href=\"poems/"+data.title+"\" class=\'list-group-item\'>"+data.title +" -"+data.author+"</a>");
        });
    });

    $(".nav-bar-btn").toggleClass("active");
});



