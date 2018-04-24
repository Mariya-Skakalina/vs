from django.urls import path
from .views import Verses, DetailVerse, FilterVerse, Home, Biography

urlpatterns = [
    path('verses', Verses.as_view(), name='Verses'),
    path('verse/<slug:pk>/', DetailVerse.as_view(), name='DetailNews'),
    path('genre/<slug:pk>/', FilterVerse.as_view(), name='filterverse'),
    path('', Home.as_view(), name='Home'),
    path('biography', Biography.as_view(), name='Biography'),
]