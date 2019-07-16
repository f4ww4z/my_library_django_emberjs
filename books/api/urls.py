from django.urls import path
from .views import BookAPIView

app_name = "api-books"

urlpatterns = [
    path("", BookAPIView.as_view(), name='book-create')
]
