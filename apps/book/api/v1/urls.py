from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet

app_name = 'book'

router = routers.SimpleRouter()
router.register('', BookViewSet, 'books')

urlpatterns = [

              ] + router.urls
