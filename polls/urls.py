from django.urls import path
from .views import ListBookApiView,DetailUpdateDestroyBookView

urlpatterns = [
    path('all/', ListBookApiView.as_view()),
    path('detail/<int:pk>/',DetailUpdateDestroyBookView.as_view())
]