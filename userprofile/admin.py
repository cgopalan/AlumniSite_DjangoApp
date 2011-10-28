from django.contrib import admin
from hartleyssite.userprofile.models import UserProfile, PAYMENT_METHOD_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	extra = 1
	
class CustomUserAdmin(UserAdmin):
	inlines = [UserProfileInline]
	list_display = ('username', 'email', 'first_name', 'last_name', 
			'is_staff', 'id', 'batch', 'payment_amount', 'payment_method')
	def batch(self, obj):
		return obj.userprofile.batch

	def payment_amount(self, obj):
		return obj.userprofile.payment_amount

	def payment_method(self, obj):
		return obj.userprofile.get_payment_method_display()

admin.site.register(User,CustomUserAdmin)
