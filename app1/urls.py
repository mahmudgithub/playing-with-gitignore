from django.urls import path
from.views import one,two

urlpatterns = [
    path('api/',one.as_view()),
    path('api/<int:pk>/',two.as_view()),
]
