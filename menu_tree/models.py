from django.db import models

class MainMenu(models.Model):
    main_menu_title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.main_menu_title

class SubMenu(models.Model):
    sub_menu_title = models.CharField(max_length=200)
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_menu_title