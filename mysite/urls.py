from django.contrib import admin
from django.urls import path, include
from core import views as core_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', core_views.HomeView.as_view(), name='home'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

    path('settings/', core_views.SettingsView.as_view(), name='settings'),
    path('settings/password/', core_views.password, name='password'),
]




