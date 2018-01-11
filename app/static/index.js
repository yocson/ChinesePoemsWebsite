$(document).ready(function () {
    var title = decodeURI(document.URL.split('/').pop());
    $.getJSON("../static/poems.json",function(result){
        // $.each(result, function(i, data){
        //     if (data.title == title){
        //         $(".author").append(data.author);
        //         $(".poem").append(data.poem.replace(/\。/g,"\。</br>"));
        //     };
        // });
        for (var i = 0; i < 4; i++){
            var rand = Math.floor(Math.random() * result.length)
            console.log(result[rand]);
            var str1 = "<h3>" + result[rand].title + "-" + result[rand].author+ "</h3><br>";
            var str2 = "<p>" + result[rand].poem.replace(/\。/g,"\。</br>")+ "</p>";
            var str = "<div class=\"col-lg-3 col-md-6 column\">" + str1 + str2 + "</div>";
            $(".randomPoems").append(str);
        }
    });
});