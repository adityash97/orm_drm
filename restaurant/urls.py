from django.urls import path
from .views import RestaurantAPIView, RatingGenericAPIView,SalesGenericAPIView,RestaurantRatingAPIView,RestaurantSalesAPIView,TopFiveRestaurantByRating,HighestTotalIncomeRestaurant
from .views import RestaurantModelViewSet,RatingViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'restaurant_viewset',RestaurantModelViewSet, basename='restaurant_viewset')
router.register(r'rating_viewset',RatingViewset,basename='rating_viewset')

urlpatterns = [
    path('', RestaurantAPIView.as_view(), name='restaurant_get_api_view'),
    path('<int:pk>/',RestaurantAPIView.as_view(), name='restaurant_update_api_view'),
    path('<int:pk>/ratings/',RestaurantRatingAPIView.as_view(),name='restaurant_ratings'),
    path('<int:pk>/sales/',RestaurantSalesAPIView.as_view(),name='restaurant_sales'),
    path('top-five/',TopFiveRestaurantByRating.as_view(),name='restaurant_top_five_by_rating'),
    path('high-sale/',HighestTotalIncomeRestaurant.as_view(),name="restaurant_by_high_sale"),
    
    path('rating/',RatingGenericAPIView.as_view(), name='rating_generic_api_view'),
    
    path('rating/<int:pk>/',RatingGenericAPIView.as_view(), name='rating_generic_update_delete_retrieve_api_view'),

    path('sales/',SalesGenericAPIView.as_view(),name='sale_generic_api_view'),
    path('sales/<int:pk>/',SalesGenericAPIView.as_view(),name='sale_generic_update_delete_retrieve_api_view'),
    
    ]

urlpatterns+=router.urls