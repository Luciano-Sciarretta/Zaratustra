from django.db import models
from datetime import datetime
from django.utils.html import format_html

class Query(models.Model):

    ANSWERED = "answered"
    NOT_ANSWERED = "not answered"
    IN_PROGESS = "in progress"
    QUERY_STATUSES = (
        (ANSWERED , "answered"),
        (NOT_ANSWERED , "not answered"),
        (IN_PROGESS , "in progress"),
    )
    name = models.CharField(max_length=50, blank = True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank = True, null=True)
    query_statuse = models.CharField(max_length=12, blank = True, null=True, choices=QUERY_STATUSES, default=NOT_ANSWERED)
    phone = models.CharField(max_length=50, blank = True, null=True)
    date = models.DateField(default=datetime.now, blank=True, editable= True)

    def __str__(self):
        return self.name
    
    
    def query_of_statuse(self,):
        if self.query_statuse == "answered":
            return format_html("<span style= 'background-color: #0a0; color:#fff;  padding: 5px;'>{}</span>", self.query_statuse)
        elif self.query_statuse == "not answered":
            return format_html("<span style= 'background-color: #a00; color:#fff;  padding: 5px;'>{}</span>", self.query_statuse)
        elif self.query_statuse == "in progress":
            return format_html("<span style= 'background-color: #FOB203; color:#000;  padding: 5px;'>{}</span>", self.query_statuse)

class Answer(models.Model): 

    query = models.ForeignKey(Query(), on_delete=models.CASCADE, blank = True, null=True)
    answer = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.now, blank=True, editable= True)

    def create_message(self,):
        # Accedo a la clase Query utilizando objects.get(), que es un método de acceso directo de QuerySet de Django. Este método busca un objeto Query en la base de datos que tenga el id igual al id de la consulta asociada (self.query.id). Esto se hace para obtener el objeto Query al que pertenece la respuesta actual.
        change_query_state = Query.objects.get(id=self.query.id)
        #El siguiente es el objeto(instancia de Query() que se obtuvo desde la db. Se actualiza el atributo  a "answered")
        change_query_state.query_statuse = "answered"
        #Finalmente se guarda ese mismo objeto en la db  cocn el estado de consulta actualizado
        change_query_state.save()
        #Lógica de envío de mail



    #Método save() de models.Model sobrecargado
    def save(self, *args, **kwargs):
        self.create_message()
        force_update = False
        if self.id:
            force_update= True
        #Con super ejecuto el método save() original de la clase padre(models.Model)    
        super(Answer, self).save(force_update=force_update)