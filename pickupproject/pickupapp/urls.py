from django.urls import path
from . import views

urlpatterns = [
    path('pickup/',views.ScheduleListView.as_view(),name='pickup'),
    path('place/',views.PlaceListView.as_view(),name='place'),
    path('member/',views.MemberListView.as_view(),name='member'),
    path('create_schedule/',views.ScheduleCreateView.as_view(),name='create_schedule'),
    path('create_place/',views.PlaceCreateView.as_view(),name='create_place'),
    path('create_member/',views.MemberCreateView.as_view(),name='create_member'),
    path('update_schedule/<int:pk>/',views.ScheduleUpdateView.as_view(),name='update_schedule'),
    path('update_place/<int:pk>/',views.PlaceUpdateView.as_view(),name='update_place'),
    path('update_member/<int:pk>/',views.MemberUpdateView.as_view(),name='update_member'),
    path('delete_schedule/<int:pk>/',views.ScheduleDeleteView.as_view(),name='delete_schedule'),
    path('delete_place/<int:pk>/',views.PlaceDeleteView.as_view(),name='delete_place'),
    path('delete_member/<int:pk>/',views.MemberDeleteView.as_view(),name='delete_member'),
]