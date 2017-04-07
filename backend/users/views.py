from django.shortcuts import render
from users.models import users
from rest_framework import viewsets
from users.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = users.objects.all().order_by('date_created')
	serializer_class = UserSerializer

