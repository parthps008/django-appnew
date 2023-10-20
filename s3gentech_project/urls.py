from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('s3gentech_app.urls')),  # Include the app's URL patterns
]