from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'users'
urlpatterns = [
    path('',views.index , name='base' ),
    path('register/',views.register , name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name = 'users/login.html') , name='login' ),
    path('logout/',authentication_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout' ),
    path('users/profile/',views.profile_page, name='profile'),
    path('users/profileForm/',views.profile_form, name='profileForm'),
    path('users/dashboard/',views.dashboard , name='dashboard')
]


urlpatterns += [
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)