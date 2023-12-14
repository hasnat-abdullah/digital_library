from django.urls import path, include

app_name = 'authentication'

urlpatterns = [
    path('api/v1/authentication/', include('apps.authentication.api.v1.urls', namespace='v1')),
]
