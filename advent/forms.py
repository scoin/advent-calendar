from django.forms import ModelForm
from advent.models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']