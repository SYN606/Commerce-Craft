from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("create_account", views.create_account, name="create_acc"),
    path("logout", views.logout_user, name="logout"),
    path("delete_user_account", views.delete_account, name="delete_acc"),
]
