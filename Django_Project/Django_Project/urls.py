from django.contrib import admin
from django.urls import path,include
import index_app, retailer
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('',include('index_app.urls')),
    path('admin/', admin.site.urls),
    path('retailer/',include('retailer.urls')),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
