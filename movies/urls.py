from django.urls import path

from .views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]