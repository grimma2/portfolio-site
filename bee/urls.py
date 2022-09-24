from django.urls import path
from .views import *
from .models import *


urlpatterns = [
	path('login/', Login.as_view(), name = 'login'),
	path('register/', Register.as_view(), name = 'register'),
	path('logout', logout_user, name = 'logout'),
	path('marafondetail/<slug:marafon_slug>', MarafonDetail.as_view(), name = 'marafon_detail'),
	path('marafonaddplace/<slug:marafon_slug>/', addplace, name = 'marafonaddplace'),
]