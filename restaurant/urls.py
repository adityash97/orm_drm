from django.urls import path
from .views import RestaurantAPIView, RatingGenericAPIView,SalesGenericAPIView,RestaurantRatingAPIView,RestaurantSalesAPIView
urlpatterns = [
    path('', RestaurantAPIView.as_view(), name='restaurant_get_api_view'),
    path('<int:pk>/',RestaurantAPIView.as_view(), name='restaurant_update_api_view'),
    path('<int:pk>/ratings/',RestaurantRatingAPIView.as_view(),name='restaurant_ratings'),
    path('<int:pk>/sales/',RestaurantSalesAPIView.as_view(),name='restaurant_sales'),
    
    path('rating/',RatingGenericAPIView.as_view(), name='rating_generic_api_view'),
    
    path('rating/<int:pk>/',RatingGenericAPIView.as_view(), name='rating_generic_update_delete_retrieve_api_view'),

    path('sales/',SalesGenericAPIView.as_view(),name='sale_generic_api_view'),
    path('sales/<int:pk>/',SalesGenericAPIView.as_view(),name='sale_generic_update_delete_retrieve_api_view')
    ]