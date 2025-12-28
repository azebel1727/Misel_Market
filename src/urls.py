from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.gallery_dashboard, name='dashboard'),
    path('upload/', views.upload_art, name='upload_art'), # New Upload Page
    path('delete/<int:art_id>/', views.delete_art, name='delete_art'), # Delete Action
    path('buy/<int:art_id>/', views.buy_art, name='buy_art'),

]