# users/urls.py


from users.views import dashboard, user_login, register_request
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path(r"dashboard/", dashboard, name="dashboard"),
    path(r"login/", user_login, name="login"),
    path(r"register/", register_request, name="register"),
    #path('login/', auth_views.LoginView.as_view(template_name="Login01.html"), name="login"),
   # path('contact/', views.contact, name='contact'),
   # path('register/', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/dashboard'), name='logout'),
   # path("register", views.register_request, name="register")
]