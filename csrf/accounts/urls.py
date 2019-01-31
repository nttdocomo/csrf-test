from django.conf.urls import url

#from accounts import views

urlpatterns = [
    url(r'^login/$', 'accounts.views.login', name='login'),
]