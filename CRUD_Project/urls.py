"""
URL configuration for CRUD_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view_All_Student/',views.view_All_Student, name ="view_All_Student"),
    path('addStudent/',views.addStudent, name = "addStudent"),
    path('searchStudent/',views.searchStudent, name = "searchStudent"),
    path('updateStudent/',views.updateStudent, name = "updateStudent"),
    path('editStudent/<int:pk>/',views.editStudent, name="editStudent"),
    path('deleteStudent/',views.deleteStudent, name = "deleteStudent"),
    path('studentportal/',views.login_view, name = "login"),
    path('register/',views.register_view, name = "register"),
    path('logout_view/',views.logout_view, name = "logout"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
