from django.urls import path

from accounts import views
from dashboard.views import  dashboard
app_name = 'accounts'
urlpatterns = [
	path('', dashboard, name='dash'),
	path('login/', views.login_view, name='login'),
	# path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
	]