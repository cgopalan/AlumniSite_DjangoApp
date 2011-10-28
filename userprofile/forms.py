from django.forms import ModelForm
from hartleyssite.userprofile.models import UserProfile

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('payment_amount', 'payment_method', 'user')
