from django.contrib import admin
from django.urls import path
from main.views import index
from usersApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path("registration/", registrationWindow, name = "registration"),
    path("registration/reg/", reg, name = "reg"),
    path("login/", login, name="login"),
    path("profile/", profile, name = "profile"),
    path("profile/<int:institutionID>/", profile, name = "pc_inst"),
    path("profile/add_pc/", add_pc, name='addPC'),
    path("profile/add_institution/", add_institution, name="addInst"),
    path("profile/edit_pc/", edit_pc, name = "edit_pc"),
    path("profile/delete_pc/",delete_pc, name = "delete_pc"),
    path("profile/delete_institution/",delete_institution, name = "delete_institution"),
    path("profile/edit_institution/",edit_institution, name = "edit_institution"),
    path("profile/add_user/",add_user, name = "add_user"),
]
