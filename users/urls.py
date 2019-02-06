from django.urls import path

from . import views

urlpatterns = [
    path(
        route='login/',
        view=views.login,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='updateprofile'
    )
]