from users.models import users
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = users
		fields = ('name', 'total_leaves', 'date_created')
		