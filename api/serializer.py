from books.models import Book
from rest_framework import serializers

class ZaratustraRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"