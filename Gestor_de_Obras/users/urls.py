from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.create_user_view, name = 'create_user_view'), #signup_view
    path('login/',views.login_view, name = 'login_view'),
    path('logout/',views.logout_view, name = 'logout_view'),
    path('list/', views.user_list_view, name='list'),

]
