from django.urls import path
from .views import NoteListCreateAPIView

urlpatterns = [
    path('', NoteListCreateAPIView.as_view()),
]
