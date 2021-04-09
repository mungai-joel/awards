from django.conf.urls import url,include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^new/project$',views.new_project,name='new-project'),
    url(r'^project/review/(\d+)',views.project_review,name='project_review'),
    url(r'^search/',views.search_project, name='search_results'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'}),
    # url(r'logout/', auth_views.logout.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
