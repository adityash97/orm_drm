from .models import Restaurant, Rating, Sale
from rest_framework import serializers
from django.utils import dateparse
from rest_framework.reverse import reverse
from django.db import models
# validators


class RestaurantNameField(serializers.Field):
    
    def to_representation(self,instance):
        return instance.restaurant.name
class RatingSerializer(serializers.ModelSerializer):
    """
    6.	Add a field in the Rating serializer that gives the name of the restaurant.
    
    1.
    One way is to use SerializerMethodField.
    2. 
    Another way is to create a serializer field/CharField and use source attribute to populate it.

    
    """
    restaurant_name = serializers.SerializerMethodField()
    restaurant_name_field = RestaurantNameField(source = '*',read_only=True)
    restaurant_char_field = serializers.CharField(source='restaurant.name',read_only=True)
    def get_restaurant_name(self,object):
        return object.restaurant.name
    
    # def validate_rating(self,obj):
    #     if obj >= 1 and obj <=5:
    #         return obj
    #     raise serializers.ValidationError("Rating must be greater than 1 and less than 5")
    
    
    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

    
    def update(self,instance, validated_data):
        instance.user = validated_data.get('user',instance.user)
        instance.restaurant = validated_data.get('restaurant',instance.restaurant)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
    
    class Meta:
        model = Rating
        fields = [ "rating", "restaurant", "user",
            "restaurant_name", "restaurant_name_field", "restaurant_char_field"]



# Normal Serializers
class RestaurantSerializer(serializers.ModelSerializer):
    
    open_year = serializers.SerializerMethodField(read_only=True)
    average_rating = serializers.DecimalField(source='avg_rating',read_only=True,max_digits=3,decimal_places=1)
    ratings  = RatingSerializer(read_only=True,many=True)
    # to_update = serializers.HyperlinkedIdentityField(view_name='restaurant_update_api_view',  lookup_field='id' )
    to_update_url = serializers.SerializerMethodField(read_only=True)
    rating_count = serializers.CharField(source='count_rating')
    total_sales = serializers.SerializerMethodField(read_only=True)
    
    
    
    
    # method fields
    def get_total_sales(self,object):
        try:
            return object.get('total_sales')
        except:
            return None
        
    def get_to_update_url(self,object):
        # sometimes getting object from other views instead of model instance. like from : TopFiveRestaurantByRating 
        try:
            id = object.id
        except:
            id = object.get('id')
        request = self.context.get('request')
        return reverse(
            viewname='restaurant_update_api_view',request=request,kwargs={'pk':id}
                       )
        
    def get_open_year(self,object):
        try:
            open_date = object.date_opened
        except:
            open_date = object.get('date_opened',None)
        if open_date:
            return dateparse.parse_date(str(open_date)).year
        return open_date
        
    # field validations
    def validate_name(self,data):
        # name must not start with numeric letters
        if data and data[0].isdigit():
            raise serializers.ValidationError('Name must not  start with number.')
        return data
    
    # format output
    def to_representation(self,instance):
        repr = super().to_representation(instance)
        # 12hr time format
        open_time = dateparse.parse_time(str(repr['open_time']))
        repr['open_time'] = open_time.strftime("%I:%M:%S %p")
        return repr

        
    class Meta:
        model=Restaurant
        fields="__all__"
        read_only_fileds = ['id','date_opened']




class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields="__all__"






