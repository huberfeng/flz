    //return_top
	 $(window).scroll(function(){
                if ($(window).scrollTop()>100){
                    $("#return_top").fadeIn(500);
                }
                else
                {
                    $("#return_top").fadeOut(500);
                }
            });

	  $("#return_top").click(function(){
                $('body,html').animate({scrollTop:0},1000);
                return false;
            });


 	//random tag colors

	var tag_class=["label-default","label-success","label-primary","label-danger","label-info","label-warning"];
	$("#tags a span").each(function(){
		var rand=parseInt(Math.random()*6);
		$(this).addClass(tag_class[rand]);

	});

	$(".tag span").each(function(){
		var rand=parseInt(Math.random()*6);
		$(this).addClass(tag_class[rand]);
		$(".tag span.glyphicon").removeClass(tag_class[rand]);
	});