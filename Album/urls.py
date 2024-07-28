
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('albumform/',views.AlbumFormView.as_view(),name='albumform'),
    path('registration/',views.RegistrationFormView.as_view(),name = 'registration'),
    path('login/',views.LoginFormView.as_view(),name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logoutt'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('albumform/<int:pk>/',views.AlbumEditFormView.as_view(),name='albumeditform'),
    path('albumeditform/<int:pk>/',views.AlbumEditFormView.as_view(),name='albumeditform'),
    path('albumdeleteform/<int:pk>/',views.AlbumDeleteFormView.as_view(),name='albumdeleteform'),

]
