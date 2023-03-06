from django.contrib import admin
from .models import MainMenu, SubMenu


class SubMenuInline(admin.StackedInline):
    model = SubMenu
    extra = 3


class MainMenuAdmin(admin.ModelAdmin):
    inlines = [SubMenuInline]

admin.site.register(MainMenu, MainMenuAdmin)