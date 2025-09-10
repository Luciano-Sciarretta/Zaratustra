from django import template
register = template.Library()


@register.filter(name="on_order")
def on_order(book, order):
    keys = order.keys()
    for name in keys:
        if name == book.title:
            return "Agregado"
        
    return "Agregar al carrito"