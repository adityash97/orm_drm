from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerilaizer,AuthorSerializer,PubdateSerializer
from django.views.generic import TemplateView
from testApp.models import Books,Author,PubDate
from django.forms import modelformset_factory
from .forms import BookForm
from rest_framework.reverse import reverse
# generic views import
from rest_framework import generics

class AuthorView(APIView):
    def get(self,request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset,many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)

class PubDateView(APIView):
    def get(self,request):
        return Response("Get is working fine")
    
    def post(self,request):
        pass
    
    
class BooksAPIView(APIView):
    def get(self,request,pk=None): #Read
        if pk:
            try:
                books=BookSerilaizer(Books.objects.get(pk=pk),context={"request": request})
            except Books.DoesNotExist:
                return Response({'error':'Book doesnot exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:    
            # breakpoint()
            books = BookSerilaizer( Books.objects.all(),many=True,context={"request": request})
        
        return Response(books.data)
    
    def post(self,request): #Create
        book = BookSerilaizer(data = request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data)
    
    def put(self,request,pk): #Update
        try:
            instance = Books.objects.get(pk=pk)
        except:
            return Response({"error":"Book does not exist"},status=status.HTTP_404_NOT_FOUND)
        book = BookSerilaizer(instance,request.data)
        if book.is_valid():
            book.save()
            return Response(book.data,status=status.HTTP_201_CREATED)
        return Response(book.errors,status=status.HTTP_400_BAD_REQUEST)
        
            
    
    def delete(self,request,pk=None): # delete
        try:
            instance = Books.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error':"Books doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message':f'Book of id {pk} is deleted.'}, status=status.HTTP_200_OK)
        


class BookView(TemplateView):
    template_name = "books.html"
    def get(self, request, *args, **kwargs):
        BookFormSet = modelformset_factory(Books, fields=('name',), extra=1) 
        formset = BookFormSet()
        return self.render_to_response({'formset': formset})
    def post(self, request, *args, **kwargs):
        BookFormSet = modelformset_factory(Books, form=BookForm, extra=1)
        formset = BookFormSet(request.POST, prefix='books')  # 👈 important!
        if formset.is_valid():
            formset.save()
        return self.render_to_response({'formset': formset})

# Practice of concrete view class
class AuthorListCreateConcreteView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AutorUpdateDetailDistroyConcreteView(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        
        redirect_url =  reverse('concrete_author_create_list',request=request)
        
        return Response({'detail':"Author deleted successfully", "redirect_to":redirect_url},status=status.HTTP_200_OK)
       
