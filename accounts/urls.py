from . import views
from django.urls import path
urlpatterns = [
  path('signup', views.signup, name='signup'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('load_profile',views.load_profile, name='load_profile'),
  path('upload_profile',views.upload_profile, name='upload_profile'),
  path('withdraw_membership',views.withdraw_membership, name='withdraw_membership'),
  path('update_player_model',views.update_player_model, name='update_player_model'),
  path('password_reset', views.password_reset, name='password_reset'),
  path('update_donation',views.update_donation, name='update_donations'),
  path('load_city',views.load_city, 'load_city')
]

#  path('signup/', views.signup, name='signup'),
#  path('login/', views.login, name='login'),
#  path('logout/', views.logout, name='logout'),
