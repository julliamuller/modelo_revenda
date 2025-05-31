
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListView, newCarCreateView, carDetailView, carUpdateView, carDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarListView.as_view(), name='cars_list'),
    path('new_car/', newCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', carDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', carUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', carDeleteView.as_view(), name='car_delete')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
