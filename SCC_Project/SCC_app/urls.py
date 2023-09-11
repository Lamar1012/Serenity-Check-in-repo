from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('serenity/check_in/guest/',views.UserCheck_in_page, name="home_page"),
    path('serenity/checked_in/users/', views.AllCheckedInUsers, name='checked-users'),
    path('serenity/clients/in_session/', views.Signed_In_Clients),
    path('serenity/sign_out/<int:guest_id>/', views.sign_out_client),
    path('serenity/new/staff/', views.CreateStaffPage),
    path('serenity/login/form/', views.staff_login_form),
    path('serenity/staff/login/', views.StaffLoginPage, name='staff-login'),
    path('serenity/staff/', views.AllStaff, name='all-staff'),
    path('serenity/logout/', views.logout_view, name='user_logout'),
    path('serenity/delete/staff/<staff_id>/', views.DeleteStaff, name='delete-staff'),
    path('serenity/edit/staff/<int:staff_id>/', views.UpdateStaff, name = 'update-form'),
    path('serenity/search_client/', views.search_clients, name = 'search-client')
]