from .models import Restaurant, Rating, Sale
from rest_framework import serializers
from django.utils import dateparse
# validators



# Normal Serializers
class RestaurantSerializer(serializers.ModelSerializer):
    
    open_year = serializers.SerializerMethodField()
    
    # method fields
    def get_open_year(self,object):
        open_date = dateparse.parse_date(str(object.date_opened))
        if open_date:
            return open_date.year
        return None
        
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

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields="__all__"






