from django.urls import path
from .views import register, user_login, submit_project, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('submit_project/', submit_project, name='submit_project'),
    path('dashboard/', dashboard, name='dashboard'),
]
