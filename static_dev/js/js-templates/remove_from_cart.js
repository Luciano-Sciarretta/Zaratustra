var csrftoken = $.cookie("csrftoken");


function csrfSafeMethod(method) {
  "use strict";
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}


$(document).ready(function () {
  $(".removeBookBtn").on("click", function (event) {
    event.preventDefault();
    console.log("Esto es complicado");
    var bookId = $(this).data("book-id");
    var $button = $(this);


    $.ajax({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
      url: "/shopping_cart/remove_from_cart/" + bookId + "/",
      type: "POST",
    
      data: { book_id: bookId },
      success: function (response) {
        if (response.status === "success") {
          $button.closest('.card-wrapper').remove();
        
          alert(response.message);

        }
        else {
          alert(response.message);
        }
      },
      error: function (xhr, status, error) {
       
        alert("Ocurrió un error al procesar la solicitud: " + error);
      }
    });
  });
});



