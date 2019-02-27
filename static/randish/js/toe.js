$(document).ready(function(){

$('.cell').on('click', function(){

    var obj = {};
    var arr = [];
    var x;
    $.each($("input[name='cell']:checked"), function(){
        x = $(this).val();
        arr.push(x);
        obj[x] = x;

    });

//    console.log(obj)

    var i;

    for(i = 0; i < arr.length; i++) {
        id = arr[i];
            $('#' + id + '+ label').html("X");
        }


     $.ajax({
         method: 'POST',
         url: "toe-ajax/",
         data: obj,
         dataType: 'json',



         success: function(data){

         zero = data.zero;

         $(zero + '+ label').html("O");

//             $('.wrapper ul').html("");
//
//             for(var i = 0; i < data.filtered_dish.length; i++) {
//                 var li = "<li><div" + " " + "class='row" + " " + "filter-list-item'><div" + " " + "class='col-sm-4'><img" +
//                 " " + "class='img-fluid'" + "src='/" + data.filtered_dish[i].image +"'></div><div" + " " +
//                 "class='col-sm-8'><h2>" + data.filtered_dish[i].dish_name + "</h2></div></div></li>"
//
//                     $('.wrapper ul').append(li);
//                 }

         }

    // });

    });

});

});
