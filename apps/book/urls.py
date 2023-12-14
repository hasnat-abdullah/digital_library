from django.urls import path, include

app_name = 'book'

urlpatterns = [
    path('api/v1/books/', include('apps.book.api.v1.urls', namespace='v1')),

]
