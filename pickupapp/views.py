from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import ScheduleModel,PlaceModel,MemberModel
from django.urls import reverse_lazy
# Create your views here.

class ScheduleListView(ListView):
    template_name='pickup.html'
    model=ScheduleModel

class ScheduleCreateView(CreateView):
    template_name='create_schedule.html'
    model=ScheduleModel
    fields=("place","member","kinds","datetime")
    success_url=reverse_lazy("pickup")

class ScheduleUpdateView(UpdateView):
    template_name='update_schedule.html'
    model=ScheduleModel
    fields=("place","member","kinds","datetime")
    success_url=reverse_lazy("pickup")

class ScheduleDeleteView(DeleteView):
    template_name='delete_schedule.html'
    model=ScheduleModel
    success_url=reverse_lazy("pickup")

class PlaceListView(ListView):
    template_name='place.html'
    model=PlaceModel

class PlaceCreateView(CreateView):
    template_name='create_place.html'
    model=PlaceModel
    fields=("name","address","tel","numbers")
    success_url=reverse_lazy("place")

class PlaceUpdateView(UpdateView):
    template_name='update_place.html'
    model=PlaceModel
    fields=("name","address","tel","numbers")
    success_url=reverse_lazy("place")

class PlaceDeleteView(DeleteView):
    template_name='delete_place.html'
    model=PlaceModel
    success_url=reverse_lazy("place")


class MemberListView(ListView):
    template_name='member.html'
    model=MemberModel

class MemberCreateView(CreateView):
    template_name='create_member.html'
    model=MemberModel
    fields=("membername","gender","tel")
    success_url=reverse_lazy("member")

class MemberUpdateView(UpdateView):
    template_name='update_member.html'
    model=MemberModel
    fields=("membername","gender","tel")
    success_url=reverse_lazy("member")

class MemberDeleteView(DeleteView):
    template_name='delete_member.html'
    model=MemberModel
    success_url=reverse_lazy("member")
        