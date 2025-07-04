from django.urls import path
from .views import BooksAPIView,AuthorView,PubDateView,BookView
from .views import AuthorListCreateConcreteView,AutorUpdateDetailDistroyConcreteView
urlpatterns = [
    path("",BooksAPIView.as_view(),name="Books"),
    path("<int:pk>/",BooksAPIView.as_view(),name="Book_Detail"),
    path("author",AuthorView.as_view(),name="Author"),
    path("pubdate",PubDateView.as_view(),name="Pubdate"),
    path("books/",BookView.as_view(),name="book_form"),
    
    
    path("concrete/author/",AuthorListCreateConcreteView.as_view(),name="concrete_author_create_list"),
    path("concrete/author/<int:pk>",AutorUpdateDetailDistroyConcreteView.as_view(),name="concrete_author_detail_update_destroy")
]