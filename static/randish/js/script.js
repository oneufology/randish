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
                var image = "url('../../" + data.daily_dishes[0].image + "')";

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
})


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
                " " + "class='img-fluid'" + "src='/" + data.filtered_dish[i].image +"'></div><div" + " " +
                "class='col-sm-8'><h2>" + data.filtered_dish[i].dish_name + "</h2></div></div></li>"

                    $('.wrapper ul').append(li);
                }

        }

    });

});


$(".navbar-toggler").click(function(){
    $(".navbar-collapse").toggleClass("show");
  });