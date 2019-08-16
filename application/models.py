from django.db import models

class EscapeRoom(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	company = models.CharField(max_length = 255)

class User(models.Model):
	username = models.CharField(max_length = 32)
	passwordHash = models.CharField(max_length = 255)
	visited = models.ManyToManyField(EscapeRoom)

	
    
class GoingOut(models.Model):
	name = models.CharField(max_length = 255)
	participants = models.ManyToManyField(User)
	decision = models.ForeignKey(EscapeRoom, on_delete=models.CASCADE)

