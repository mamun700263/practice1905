
from django.urls import path
from . import views
urlpatterns = [
    path('musicianform/',views.MusicianFormView.as_view(),name='musicianform'),
    path('musicianform/<int:pk>/',views.MusicianEditFormView.as_view(),name='musicianeditform'),

]
