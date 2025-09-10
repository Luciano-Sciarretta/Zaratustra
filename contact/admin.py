from django.contrib import admin

from .models import Query
from .models import Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QueryAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['query_of_statuse', 'name',      
            'description',
            'email', 
            'phone',
            'date']
    list_filter = ['query_statuse', 'date']

admin.site.register(Query, QueryAdmin)