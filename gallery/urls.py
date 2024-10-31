from django.urls import path
from .views import created_photo_view

app_name = 'gallery'
urlpatterns = [
    path('created_photo/', created_photo_view, name="created_photo")
]
