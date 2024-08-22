from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('user_form/', views.user_create_view, name='user_form'),
    path('user_list/', views.user_view, name="user_list"),
    path('update/<int:id>/', views.update_view, name="doc_update"),
    path('delete/<int:id>/', views.delete_view, name="doc_delete"),
]