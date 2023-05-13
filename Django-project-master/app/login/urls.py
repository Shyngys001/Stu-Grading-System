from django.urls import path
from . import views
from .views import login_view, register_view, logout_view

app_name = 'login'
urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
    