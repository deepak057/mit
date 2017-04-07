from django.db import models
from users.models import users
# Create your models here.
class leaves(models.Model):
	user = models.ForeignKey(users)
	year = models.IntegerField()
	jan = models.IntegerField(default = 0)
	feb = models.IntegerField(default = 0)
	mar = models.IntegerField(default = 0)
	apr = models.IntegerField(default = 0)
	may = models.IntegerField(default = 0)
	jun = models.IntegerField(default = 0)
	july = models.IntegerField(default = 0)
	aug = models.IntegerField(default = 0)
	sep = models.IntegerField(default = 0)
	oct = models.IntegerField(default = 0)
	nov = models.IntegerField(default = 0)
	dec = models.IntegerField(default = 0)
	total_allowed_leaves = models.IntegerField(default=12)
