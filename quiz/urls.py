
from django.urls import path
from . import views

urlpatterns = [
    path('custom-quiz/', views.custom_quiz_view, name='custom_quiz_view'),
]
