
from django.urls import path
from Session_App import views

urlpatterns = [
    path("home/", views.home_view),

    path('create_session/', views.create_session_view),
    path('delete_session/', views.delete_session_view),
    path('save_session_data/', views.save_session_data_view),
    path('access_session_data/', views.access_session_data_view),
    path('delete_session_data/', views.delete_session_data_view),
]