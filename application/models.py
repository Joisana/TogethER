from django.db import models

class EscapeRoom(models.Model):
	name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	company = models.CharField(max_length = 255) #firma
	def __str__(self):
		return '"' + self.name + '"'

class User(models.Model):
	username = models.CharField(max_length = 32)
	passwordHash = models.CharField(max_length = 255)
	visited = models.ManyToManyField(EscapeRoom, related_name="visitors") # osoby, które odwiedziły dany escape room

	def __str__(self):
		return '"' + self.username + '"'
    
class GoingOut(models.Model):
	organisator = models.ForeignKey(User, on_delete = models.CASCADE, related_name="organisedGoingOuts")
	participants = models.ManyToManyField(User, related_name="goingOuts")
	decision = models.ForeignKey(EscapeRoom, on_delete = models.CASCADE, null = True)

