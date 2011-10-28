from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response('hartleysalumni.html')

def aboutus(request):
    return render_to_response('aboutus.html')

def hartleys(request):
    return render_to_response('hartleys.html')
    
def contactus(request):
    return render_to_response('contactus.html')

def search(request):
    return render_to_response('search.html')

def login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/userprofile/")
            #return render_to_response('userprofile.html', {'user' : user})
        else:
            error = "Sorry, that's not a valid username or password"
            
    return render_to_response('login.html', {'error' : error})

def changepass(request):
    error = ''
    if request.method == 'POST':
        oldpassword = request.POST.get('oldpass', '')
        #user = User.objects.get(username=request.user.username)
        if request.user.check_password(oldpassword):
            newpassword1 = request.POST.get('newpass1', '')
            newpassword2 = request.POST.get('newpass2', '')
            if len(newpassword1) < 6:
                error = "New Password must be at least 6 characters long"
            elif (newpassword1 != newpassword2):
                error = "New passwords dont match"
            else:
                request.user.set_password(newpassword1)
                request.user.save()
                return HttpResponseRedirect("/userprofile/")
        else:
            error = "Sorry, the current password is incorrect"
    return render_to_response('changepass.html', {'error' : error})
