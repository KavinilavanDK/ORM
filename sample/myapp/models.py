from django.db import models
from django.contrib import admin
class football_player(models.Model):
    player_name=models.CharField(max_length=40)
    player_position=models.CharField(max_length=50)
    player_age=models.IntegerField()
    jersy_no=models.IntegerField()
    player_native=models.CharField(max_length=40)
class football_playerAdmin(admin.ModelAdmin):
    list_display=["player_name","player_position","player_age","jersy_no","player_native"]