from django.urls import path
from ApiTest import views

app_name = "ApiTest"
urlpatterns = [
    path('', views.UserCreateAPIView.as_view(), name="UserCreateAPIView"),
    path('login', views.LoginAPIView.as_view(), name="LoginViewAPIView"),
    path('books', views.BookAPIView.as_view(), name="Books"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="BookDetail"),
    path('borrow', views.borrow, name="borrow"),
    ]