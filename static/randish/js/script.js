$(document).ready(function(){


// PLACEHOLDER

$('#id_username').attr("placeholder", "Имя пользователя");
$('#id_password').attr("placeholder", "Пароль");
$('#id_password1').attr("placeholder", "Пароль");
$('#id_password2').attr("placeholder", "Пароль");
$('#id_ingredient_name').attr("placeholder", "Новый ингредиент");
$('#id_dish_name').attr("placeholder", "Блюдо");
$('#id_dish_type option:selected').text('Тип блюда');
$('#id_ingredients').attr("multiple", "true");




// AJAX RANDOM
$('#reload_button').on('click', function(e){
			e.preventDefault();
			$.ajax({
				method: 'Get',
				url: $(this).attr('href'),
				data: "",
				dataType: 'json',

				success: function(data){
                $('.dish-image ul').html("");

                var h1 = "<h1>" + data.daily_dishes[0].dish_name + "</h1>";
                var h4 = "<h4>(" + data.daily_dishes[0].dish_type + ")</h4>";
                var image = "url('/media/" + data.daily_dishes[0].image + "')";

                 for(var i = 0; i < data.ingr_by_dish.length; i++) {
                    var li = "<li>" + data.ingr_by_dish[i].ingredient_name + "</li>";

                    $('.dish-image ul').append(li);
                 }

                $('.dish-image h1').html(h1);
                $('.dish-image h4').html(h4);
                $('.dish-image').css("background-image", image);

            }
        })
    });


// AJAX FILTER
$('.ingr_filter').on('click', function(){
    var obj = {};
    var x;
    $.each($("input[name='ingr']:checked"), function(){
        x = $(this).val();
        obj[x] = x;
    });

    $.ajax({
        method: 'POST',
        url: "ajax/",
        data: obj,
        dataType: 'json',



        success: function(data){

            $('.wrapper ul').html("");

            for(var i = 0; i < data.filtered_dish.length; i++) {
                var li = "<li><div" + " " + "class='row" + " " + "filter-list-item'><div" + " " + "class='col-sm-4'><img" +
                " " + "class='img-fluid'" + "src='/media/" + data.filtered_dish[i].image +"'></div><div" + " " +
                "class='col-sm-8'><h2>" + data.filtered_dish[i].dish_name + "</h2></div></div></li>"

                    $('.wrapper ul').append(li);
                }

        }

    });

});

// MOBILE MENU
$(".navbar-toggler").click(function(){
    $(".navbar-collapse").toggleClass("show");
});


// TT CUP AJAX
$('#tt_cup_button').on('click', function(e){
    e.preventDefault();

    var rate = $("input[name='rate']:checked").val();
    var url = $("input[name='player_id']").val();
    var ttCupObj = {"rate": rate, "url": url};


    $.ajax({
        method: 'POST',
        url: "push/",
        data: ttCupObj,
        dataType: 'json',

        success: function(data){

            $('.tt-cup-result .player-name').html("");
            $('.tt-cup-result ul').html("");

            var name = "<h5>" + data.name + "</h5>";

            $('.tt-cup-result .player-name').append(name);

            console.log(data.report)




            for(var i = 0; i < data.report.length; i++) {
                var li = "<li>" + data.report[i]  + "</li>";

                $('.tt-cup-result ul').append(li);

            }

        }

    });

    });







});