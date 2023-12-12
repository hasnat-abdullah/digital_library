from django.urls import path, include

app_name = 'user'

urlpatterns = [
    path('api/v1/users/', include('apps.user.api.v1.urls', namespace='v1')),
]
