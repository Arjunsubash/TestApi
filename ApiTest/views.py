from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from ApiTest.serializers import UserSerializer,LoginSerializers,BookSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from ApiTest.models import Book,Borrowed_book
from twisted.spread.pb import respond
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key,"Message":'Login successfull '})
    

class BookAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
def borrow(request):
    if request.method  == "POST":
        name=request.POST['bookname']
        borrow = Book.objects.get(id=name)
        borrowdata = Borrowed_book(               
                bookname=borrow.bookname,
                )
        borrowdata.save()
        bookupdate = Book.objects.get(id=name)
        print(bookupdate)
        bookupdate.count -= 1
        bookupdate.save()
        return redirect('ApiTest:borrow')
    else:   
        BookList = Book.objects.all()
        Borrowedbook = Borrowed_book.objects.all()
        context={
            'BookList':BookList,
            'Borrowedbook':Borrowedbook
            }
        return render(request, 'books.html',context=context)







