$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2]
    console.log(eml)
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
          

            console.log("success")

        }
    })          
});
$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2]
    console.log(eml)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            console.log(data)
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
            console.log("success")

        }
    })
});




$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml=this
    console.log("Removing product:", id);

      // safer than parentNode
   // Optimistically remove the item from the DOM

    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
             prod_id: id
            },
        success: function (data) {
            
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("total_amount").innerText = data.total_amount;
            eml.parentNode.parentNode.parentNode.parentNode.remove(); // Adjust based on your HTML structure
              // clean removal
            console.log("Item removed successfully");
        },
        error: function (xhr, status, error) {
            console.error("Error removing item:", error);
        }
    });
});















// // $('#slider4').owlCarousel({
// //     loop: true,
// //     margin: 10,
// //     nav: true,
// //     responsive: {
// //         0: { items: 1 },
// //         600: { items: 3 },
// //         1000: { items: 5 }
// //     }
// // });
