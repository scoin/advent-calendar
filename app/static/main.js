gift = {'opened': false}

$(document).ready(function(){
	$('.box').click(function(e){
		if(gift['opened'] === false){
			$.post(window.location.href, function(data){
				gift = data;
				console.log(gift.gift)
				$('.box').html("<img src = '/static/box_open.png'>")
				$('.description').html("<h2>" + data.gift + "</h2>");
				if(gift.gift_type === "compliment"){
					message = "I truly feel that way."
				} else {
					message = "Now make sure to get it from me!"
				}
				$('.message').html("You opened your gift! " + message + "<br>" + "Don't forget your gift tomorrow!")
			}, 'json')
		}
	})

	$('.day').click(function(e){
		var that = this;
		$.post(window.location.href, {'gift': $(that).attr('id')}, function(data){
			if(!data['fail']){
				var p = that.children[0].children[1];
				$(p).remove();
				$(that.children[0]).append("<p>"+data.gift+"</p>");
			}
		})
	})
})
