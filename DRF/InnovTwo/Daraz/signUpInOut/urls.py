from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_reg_views, name='user_reg_views'),
]