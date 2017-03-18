function state(data){
    var items=$('li.md-links-item');
    items.each(function(sitem){
        tlink=$($('a',items[sitem])[0]).attr('href');
        if(tlink in data){
            if(data[tlink]!='200'){
                $(items[sitem]).css('opacity','0.4');
            }
        }
    });
}
void(function(){
    $.ajax({
        url:'https://cubesky.github.io/linkChecker/data.jsonp?callback=state',
        dataType:'jsonp',
        cache: false,
        state: function(data){
            console.log(data)
        } 
    });
})();