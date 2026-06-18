from django.db import models
from django.conf import settings
class Teams(models.Model):
    
    team_name = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    created_at = models.DateTimeField(auto_now_add= True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= 'created_teams', on_delete= models.CASCADE, blank= True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank= True, related_name= 'teams')
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.team_name
