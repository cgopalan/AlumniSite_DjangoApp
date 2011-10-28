from hartleyssite.userprofile.forms import UserProfileForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def userprofile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.userprofile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/search/')
	else:
		form = UserProfileForm(instance=request.user.userprofile)
	return render_to_response('userprofile.html', {'form' : form, 'user' : request.user})
		
	
