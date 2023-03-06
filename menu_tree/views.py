from django.shortcuts import render
from django.views import generic
from .models import MainMenu

class IndexView(generic.ListView):
    template_name = 'menu_tree/index.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return MainMenu.objects.all()
    

class MenuView(generic.DetailView):
    model = MainMenu
    template_name = 'menu_tree/menu.html'

    def get_queryset(self):
        return MainMenu.objects.filter()