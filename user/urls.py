from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login_view, name='login'),
    path('signup/', views.custom_signup_view, name='signup'),
    path('profile/', views.profile_edit, name='profile'),
    path('profiled/', views.profiled_view, name='profiled'),
]
