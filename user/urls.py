from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("create_account", views.create_account, name="create_acc"),
    path("logout", views.logout_user, name="logout"),
    path("delete_user_account", views.delete_account, name="delete_acc"),  # type: ignore
    path(
        "profile" + "_commerce_craft_" + "<str:username>",
        views.view_profile,
        name="profile",
    ),
    path('edit_profile' + "_commerce_craft_" + "<str:username>", views.profile_update, name='update_profile') # type: ignore
]
