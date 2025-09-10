var csrftoken = $.cookie("csrftoken");
function csrfSafeMethod(method) {
  "use strict";
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

function AddLocalStorage(bookTitle, bookId, bookValue) {
  "use strict";

  $.ajax({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },

    url: "/store/",
    type: "POST",
    data: { book_title: bookTitle, book_id: bookId, book_value: bookValue },
    success: function (response) {
      let user_cart = response.books
     

      if (response.status === "success") {
        localStorage.setItem(`Cart of ${response.user}: ` , JSON.stringify(user_cart))
        alert(response.message);

      } else {
        alert(response.message);
      }
    },
    error: function (xhr, status, error) {
      console.error("Error:", status, error);
      alert("An error occurred. Please try again.");
    },
  });
}

$(document).ready(() => {
  $("form").on("submit", function (event) {
    event.preventDefault();

    const bookTitle = $(this).find('input[name= "book_title"]').val();
    const bookId = $(this).find("input[name = 'book_id']").val();
    const bookValue = $(this).find("input[name = 'book_value']").val();
    AddLocalStorage(bookTitle, bookId, bookValue);
  });
});
