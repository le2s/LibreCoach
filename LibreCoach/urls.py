from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LibreCoach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', 'connection.views.goToForm',name='login'),
    url(r'^home', 'connection.views.goToHome'),
    url(r'^projet', 'projects.views.goToProjet'),

)
