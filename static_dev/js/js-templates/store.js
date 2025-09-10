// csrftoken:  Cross-Site Request Forgery (Falsificación de solicitudes entre sitios)
console.log("todo bien ajax")
var csrftoken = $.cookie("csrftoken");
function csrfSafeMethod(method) {
  "use strict";
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

function AgregarI(cada_producto_id, valor) {
  "use strict";

  $.ajax({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },

    url: "/store/add_localStorage/",
    type: "POST",
    data: { cada_producto_id: cada_producto_id, valor: valor },
    success: function (json) {
      console.log("json en localstorage:  ", json);
      let cantidad = json[0].cantidad.toString();
      cantidad = parseInt(cantidad);
      let idproducto = json[0].idproducto.toString();
      let bookInLocalStorage = localStorage.getItem(idproducto);
      let stock = json[0].stock;
      console.log("stock::: en funcion", stock);
      if (bookInLocalStorage !== null && parseInt(json[0].cantidad) != 0) {
        let cantidad = parseInt(json[0].cantidad);
        cantidad += 1;
        localStorage.setItem(idproducto, cantidad.toString());
      } else if (bookInLocalStorage == null) {
        localStorage.setItem(idproducto, json[0].cantidad.toString());
      } else if (cantidad == 0) {
        console.log("No hay productos disponibles");
        alert("No hay stock de ese libro");
      }
      if (!stock) {
        idproducto = idproducto.slice(4);
        console.log("stock en if:", idproducto);

        $(".agregar-" + idproducto)
          .text("Out of  Stock")
          .css("background-color", "red");
        $(".agregar-" + idproducto).prop("disabled", true);
      }
    },
    error: function (xhr, errmsg, err) {
      console.log("Error en carga de respuesta");
    },
  });

  /*Petición ajax actualizar dinamicamente el stock del libro sin tener que recargar la página*/
}

$(".agregar").click(function (event) {
  "use strict";

  event.preventDefault();
  let cada_producto_id = $(this).parent().find(".verid").val();
  let valor = $(this).parent().find(".vervalor").val();



  let i;
  for (i = 0; i < localStorage.length; i++) {
    let clave = localStorage.key(i);

    let el_valor = localStorage[clave];

    if (clave == cada_producto_id) {
      valor = el_valor;
    } else {
      console.log("no hay coincidenciaaaa");
    }
  }

  AgregarI(cada_producto_id, valor);
});


