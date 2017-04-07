from django.db import models
from django.utils import timezone

# Create your models here.

class users(models.Model):
	name = models.CharField(max_length=50)
	total_leaves = models.IntegerField(default=0) 
	date_created = models.DateTimeField( default = timezone.now)


	def __str__(self):
		return self.title