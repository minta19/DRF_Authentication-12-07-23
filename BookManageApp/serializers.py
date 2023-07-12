from rest_framework import serializers
from .models import CustomUser,Book
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['Author_name']

class Bookserializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    title=serializers.CharField(required=True,validators=[UniqueValidator(queryset=Book.objects.all())])
    class Meta:
        model=Book
        fields=['id','title','description','price','author']

    
    