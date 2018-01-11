$(document).ready(function () {
    var title = decodeURI(document.URL.split('/').pop());
    $.getJSON("../static/poems.json",function(result){
        $.each(result, function(i, data){
            if (data.title == title){
                $(".author").append(data.author);
                $(".poem").append(data.poem.replace(/\。/g,"\。</br>"));
            };
        });
    });

    $(".nav-bar-btn").removeClass("active");
});