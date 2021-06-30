from rest_framework.serializers import ModelSerializer
from demo01.models import Author,Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BooklSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'