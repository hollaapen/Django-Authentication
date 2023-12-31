from django.urls  import path
from . import views
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login', views.UserLoginPageView.as_view(), name="login"),
    path('home', views.home, name="home"),
    path('logout', views.Logout, name="logout")

]