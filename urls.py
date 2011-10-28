from django.conf.urls.defaults import *
from hartleyssite.views import *
from hartleyssite.userprofile.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hartleyssite/', include('hartleyssite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^aboutus/', aboutus),
	(r'^hartleys/', hartleys),
	(r'^contactus/', contactus),
    (r'^login/', login),
    (r'^userprofile/', userprofile),
	(r'^search/', search),
	(r'^changepass/', changepass),
    ('', index),
)
