from django.urls import path
from .views import created_photo_view, list_post_view

app_name = 'gallery'
urlpatterns = [
    path('created_photo/', created_photo_view, name="created_photo"),
    path('list_posts/', list_post_view, name="list_posts"),
]
