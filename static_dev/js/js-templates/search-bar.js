//  Para traer el libro seleccionado en la barra de búsqueda

var csrftoken = $.cookie("csrftoken");
function csrfSafeMethod(method) {
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

$(document).ready(function () {
  $("#search-button-id").click(function () {
    console.log("antes de asignar value");
    value = $("#id_querycom").val();
    console.log("VAlue:::", value);
    show_product(value);
  });
});
function show_product(value) {
  $.ajax({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
    url: "/show_book/",
    type: "GET",

    data: { value: value },

    success: function (json) {
      console.log("Todo bien en ajax adebtri de show_product");
      return_value =
        "<h2 style='text-align:center;'>" +
        json[0].title +
        "</h2>" +
        "<img style='width:100%;' src='" +
        json[0].cover_image +
        "'/>";
      $("#searchbar-book-container").html(return_value);
      $(".hide").hide();

      console.log(json[0].title);
    },
    error: function (xhr, errmsg, err) {
      console.log("Error en carga de respuesta");
    },
  });
}
