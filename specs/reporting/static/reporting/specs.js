// A $( document ).ready() block.
$( document ).ready(function() {
    //highlight navbar item
    var path = window.location.pathname;
    $("#site-nav").children().each(function(key, li){
        var search = $(li).find('a');
        if( search.length > 0){
            var a = search[0];
            if(path === $(a).attr('href')){
                console.log('found the a');
                $(a.parentNode).addClass('active');
            }
        }   
    });
});
