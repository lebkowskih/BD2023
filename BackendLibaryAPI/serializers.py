from rest_framework import serializers

from .models import Book,Author,Category,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'name','email','password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name', 'surname','birthday','nationality','author_description')
        #extra_kwargs = {'books': {'required': True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'category_description')
        #extra_kwargs = {'books': {'required': False}}
 
class BookSerializer(serializers.ModelSerializer):
    #authors = AuthorSerializer()
    #categories = CategorySerializer()
    class Meta:
        model = Book
        fields = ('id','title','isbn','date_of_publication','quantity','book_description','language','authors','categories')
        ordering = ['name']
        # extra_kwargs = {'authors': {'required': True} ,'categories':{'required': True}}

