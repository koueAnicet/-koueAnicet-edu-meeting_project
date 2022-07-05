from django.urls import path
from Site import views

urlpatterns = [
    path('',views.home, name="home"),
    path('meeting-details/',views.meeting_detail, name="meeting_details"),
    path('meetings/',views.meetings, name="meetings"),

]