# urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('create/', views.create_dataset, name='create_dataset'),
    path('datasets/', views.dataset_list, name='list_dataset'),
    path('datasets/<int:pk>/', views.dataset_detail, name='dataset_detail'),
    path('datasets/<int:pk>/delete/', views.dataset_delete, name='dataset_delete'),
    path('download_images/<int:dataset_id>/', views.download_images, name='download_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)