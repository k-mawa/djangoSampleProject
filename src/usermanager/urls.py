from django.urls import path
from . import views
from .views import *

app_name = 'usermanager'

urlpatterns = [
	#path('my_private_info', views.my_private_info, name='my_private_info'),
	#path('my_private_info_edit', views.my_private_info_edit, name='my_private_info_edit'),
	#path('activate/<str:activationkey>', NewUserActivateView.as_view()),
	#path('pass_recover/<str:activationkey>', pass_recover),
    path("", views.Index.as_view(), name="index")
]
