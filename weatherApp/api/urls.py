from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('api/',views.ExternalAPIExampleView.as_view()),  
]
