
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.views.generic import TemplateView

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='index.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='index.html'), name='services'),
    path('services/web/', TemplateView.as_view(template_name='index.html'), name='web-dev'),
    path('services/design/', TemplateView.as_view(template_name='index.html'), name='design'),
    path('contact/', TemplateView.as_view(template_name='index.html'), name='contact'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
