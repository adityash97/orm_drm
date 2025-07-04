from testApp.models import Author,Books,PubDate
from rest_framework import serializers
from rest_framework.reverse import reverse
def testValidator(value):
    if 'aditya' not in value:
        return value
    raise serializers.ValidationError("name contain's aditya")
class AuthorSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255,validators=[testValidator])
    to_update = serializers.SerializerMethodField()
    
    def create(self,validated_data):
        instance = Author.objects.create(**validated_data)
        return instance
    
    def validate(self, data):
        if len(data['name']) <= 3:
            raise serializers.ValidationError({'name':"Autor name must have more than 3 chars."})
        elif any(c.isdigit() for c in data['name']):
            raise serializers.ValidationError('Name should not contain any number.')
        return data
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',None)
        instance.save()
        return instance
    
    def get_to_update(self,obj):
        # view = self.context.get('view')
        # breakpoint()
        return reverse('concrete_author_detail_update_destroy',kwargs={'pk':obj.id},request=self.context['request'])
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     view = self.context.get('request')
    #     url_name = getattr(getattr(view.request, 'resolver_match',None),'url_name',"")
    #     if url_name == 'concrete_author_detail_update_destroy':
    #         data.pop('to_update')
    #     return data
            
        

class PubdateSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    date = serializers.DateField()

#TODO : Write notes on serializer.CustomRelationShip.This is one wa of reverse relationship
class PBListingField(serializers.RelatedField):
    def to_representation(self,instance):
        return instance.date
    
class BookSerilaizer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    author = serializers.PrimaryKeyRelatedField(queryset= Author.objects.all())
    # pub_date=serializers.PrimaryKeyRelatedField(queryset= PubDate.objects.all(),many=True) # as list of pubdate id will be coming from frontend
    tracks = PBListingField(many=True,read_only=True)
   
    #         {
    #     "name": "Aditya's book",
    #     "author": 2,
    #     "pub_date": [1]
    # }

    
    
    def to_representation(self,instance):
        repr = super().to_representation(instance)
        # breakpoint()
        repr['author'] = AuthorSerializer(instance.author,context=self.context).data
        repr['pub_date'] = PubdateSerializer(instance.pub_date,many=True).data
        return repr
        
    
    def create(self,validated_data):
        pub_dates = validated_data.pop('pub_date')
        book_instance = Books.objects.create(**validated_data)
        book_instance.pub_date.set(pub_dates)
        return book_instance
    
    
        
    def update(self,instance , validated_data):
        pub_dates = validated_data.get('pub_date')
        instance.name = validated_data.get('name',instance.name)
        instance.author = validated_data.get('author',instance.author)
        if pub_dates:
            instance.pub_date.set(pub_dates)
        instance.save()
        return instance
            
        
        
    
    


