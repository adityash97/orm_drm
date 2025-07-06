from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantSerializer,RatingSerializer,SaleSerializer
from .models import Restaurant,Rating,Sale
from django.db.models import Avg

# Restaurant View
class RestaurantAPIView(APIView,PageNumberPagination):
    queryset = Restaurant.objects.all()

    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            serializer = RestaurantSerializer(get_object_or_404(Restaurant,pk=pk),context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        type_filter = request.GET.getlist('type',[])
        if type_filter:
            self.queryset = self.queryset.filter(restaurant_type__in = type_filter)
        self.queryset = self.queryset.annotate(avg_rating = Avg('ratings__rating'))
            
        self.page_size = 5 
        paginated_ratings = self.paginate_queryset(self.queryset, request)
        serializer = RestaurantSerializer(paginated_ratings, many=True,context={'request': request})
        return self.get_paginated_response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = RestaurantSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None,*args,**kwargs):
        queryset = get_object_or_404(Restaurant,pk=pk)
            
        serializer = RestaurantSerializer(data=request.data, instance = queryset)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self,request,pk=None,*args,**kwargs):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        restaurant.delete()
        return Response({"message":f"Restaurant of id : {pk} deleted."},status=status.HTTP_200_OK)
        
class RestaurantRatingAPIView(APIView,PageNumberPagination):
    def get(self,request,pk=None,*args,**kwargs):
        self.page_size = 10
        restaurant = get_object_or_404(Restaurant,pk=pk)
        rating_queryset = self.paginate_queryset(restaurant.ratings.all(),request=request)
        
        serializer = RatingSerializer(rating_queryset,many=True)
        
        return self.get_paginated_response(serializer.data)
        
             
class RestaurantSalesAPIView(APIView,PageNumberPagination):
    def get(self,request,pk=None, *args,**kwargs):
        self.page_size = 5
        restaurant = get_object_or_404(Restaurant,pk=pk)
        sales_queryset = self.paginate_queryset(restaurant.sales.all(),request)
        serializer = SaleSerializer(sales_queryset,many=True)
        return self.get_paginated_response(serializer.data)
        
# Rating View
class RatingGenericAPIView(GenericAPIView,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request=request,*args,**kwargs)
    
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def put(self, request, pk=None,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,pk=None,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# Sales View
class SalesGenericAPIView(GenericAPIView,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request=request,*args,**kwargs)
    
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def put(self, request, pk=None,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,pk=None,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    
    
    
    

# {
#             "name": "ATestRest1",
#             "website": "http://test-rest.com/",
#             "open_time": "12:20:05",
#             "date_opened": "2020-07-30",
#             "latitude": -36.6052075,
#             "longitude": -97.945041,
#             "restaurant_type": "IN"
#         }

{
            "id": 31,
            "open_year": 2017,
            "name": "Rodriguez, Figueroa And Sanchez with Chicken",
            "website": "http://www.yang.com/",
            "open_time": "03:20:43",
            "date_opened": "2017-09-08",
            "latitude": 45.655277,
            "longitude": 143.206344,
            "restaurant_type": "FF"
        },