
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path ('blog/', views.post_deails, name = 'post_deails' ),
    path('category/<slug:category_slug>/', views.category_deails, name ='category_deails'),
    ]