gift = {'opened': false}

$(document).ready(function(){
	$('.box').click(function(e){
		if(gift['opened'] === false){
			$.post(window.location.href, function(data){
				gift = data;
				console.log('works!')
				$('.box').attr("src", '/static/box_open.png');
				$('.description').html("<h2>"+gift.gift+"</h2>");
			}, 'json')
		}
	})
})