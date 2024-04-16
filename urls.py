from django.contrib import admin
from django.urls import path
from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    
    path('', views.loginn, name='login'),
    path('signup',views.signup,name="signup"),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard',views.employee_dashboard,name='employee_dashboard'),
    path('employee_dashboard/add',views.add,name='add'),
    path('employee-details',views.employee_details,name='employee-details'),
    path('<int:id>', views.view_employee, name='view_employee'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('attend_delete/<int:id>/', views.attend_delete, name='attend_delete'),
    path('month_delete/<int:id>/', views.month_delete, name='month_delete'),
    path('add', views.add, name='add'),
    path('attendance-details',views.attendance_details,name='attendance-details'),
    
    path('view-month',views.display_months,name='view-month'),
    path('create_leave',views.leave_creation,name='createleave'),
    path('create_permission',views.permission_creation,name='createpermission'),
    path('permission',views.permission,name='permission'),
    path('request',views.request,name='request'),
    path('profile',views.profile,name='profile'),
    path('attendance',views.attendance,name='attendance'),
    path('leave_request',views.leave_request,name='leave_request'),
    path('permission_request',views.permission_request,name='permission_request'),
    path('change_password',views.change_password,name='change_password'),
    path('view-month-days',views.display_months,name='view-month-days'),
    #leave pending to all
    path('leaves/pending/all/',views.leaves_list,name='leaveslist'),
    path('leaves/pending/all/employee-details',views.employee_details,name='employee_details'),
    path('leaves/pending/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('leaves/pending/all/permission',views.permission,name='permission'),
    path('leaves/pending/all/request',views.request,name='request'),
    path('leaves/pending/all/approved',views.leaves_approved_list,name='leaves_approved_list'),
    path('leaves/pending/all/add',views.add,name='add'),

    path('leaves/approved/all/',views.leaves_approved_list,name='approvedleaveslist'),
    path('leaves/approved/all/employee-details',views.employee_details,name='employee_details'),
    path('leaves/approved/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('leaves/approved/all/permission',views.permission,name='permission'),
    path('leaves/approved/all/request',views.request,name='request'),
    path('leaves/approved/all/add',views.add,name='add'),


    path('leaves/cancel/all/',views.cancel_leaves_list,name='canceleaveslist'),
    path('leaves/cancel/all/employee-details',views.employee_details,name='employee_details'),
    path('leaves/cancel/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('leaves/cancel/all/permission',views.permission,name='permission'),
    path('leaves/cancel/all/request',views.request,name='request'),
    path('leaves/cancel/all/add',views.add,name='add'),

    path('leaves/all/view/<int:id>/',views.leaves_view,name='userleaveview'),
    path('leaves/all/view/<int:id>/',views.empleaves_view,name='empleaveview'),
    path('leaves/view/table/',views.view_my_leave_table,name='staffleavetable'),
    path('leaves/view/table/',views.view_my_leave_table,name='empleavetable'),
    path('leave/approve/<int:id>/',views.approve_leave,name='userleaveapprove'),
    path('leave/unapprove/<int:id>/',views.unapprove_leave,name='userleaveunapprove'),
    path('leave/cancel/<int:id>/',views.cancel_leave,name='userleavecancel'),
    path('leave/uncancel/<int:id>/',views.uncancel_leave,name='userleaveuncancel'),
    #path('leaves/rejected/all/',views.leave_rejected_list,name='leavesrejected'),
    path('leaves/rejected/all/employee-details',views.employee_details,name='employee_details'),
    path('leaves/rejected/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('leaves/rejected/all/permission',views.permission,name='permission'),
    path('leaves/rejected/all/request',views.request,name='request'),

    
    #path('leave/reject/<int:id>/',views.reject_leave,name='reject'),
    #path('leave/unreject/<int:id>/',views.unreject_leave,name='unreject'),


    #permission

     path('permissions/pending/all/',views.permission_list,name='permissionslist'),
    path('permissions/pending/all/employee-details',views.employee_details,name='employee_details'),
    path('permissions/pending/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('permissions/pending/all/permission',views.permission,name='permission'),
    path('permissions/pending/all/request',views.request,name='request'),
    path('permissions/pending/all/add',views.add,name='add'),
    #path('permissions/pending/all/approved',views.permissions_approved_list,name='permissions_approved_list'),
    
    path('permissions/approved/all/',views.permissions_approved_list,name='approvedpermissionslist'),
    
    path('permissions/approved/all/employee-details',views.employee_details,name='employee_details'),
    path('permissions/approved/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('permissions/approved/all/permission',views.permission,name='permission'),
    path('permissions/approved/all/request',views.request,name='request'),



    path('permissions/cancel/all/',views.cancel_permissions_list,name='cancelpermissionslist'),
    path('permissions/cancel/all/employee-details',views.employee_details,name='employee_details'),
    path('permissions/cancel/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('permissions/cancel/all/permission',views.permission,name='permission'),
    path('permissions/cancel/all/request',views.request,name='request'),
    path('permissions/cancel/all/add',views.add,name='add'),

    path('permissions/all/view/<int:id>/',views.permissions_view,name='userpermissionview'),
    
    path('permissions/view/table/',views.view_my_permission_table,name='staffpermissiontable'),
    
    #path('permission/approve/<int:id>/',views.approve_permission,name='userpermissionapprove'),
    #path('permission/unapprove/<int:id>/',views.unapprove_permission,name='userpermissionunapprove'),
    path('permission/cancel/<int:id>/',views.cancel_permission,name='userpermissioncancel'),
    path('permission/uncancel/<int:id>/',views.uncancel_permission,name='userpermissionuncancel'),
    path('permissions/rejected/all/',views.permission_rejected_list,name='permissionsrejected'),
    path('permissions/rejected/all/employee-details',views.employee_details,name='employee_details'),
    path('permissions/rejected/all/attendance-details',views.attendance_details,name='attendance_details'),
    path('permissions/rejected/all/permission',views.permission,name='permission'),
    path('permissions/rejected/all/request',views.request,name='request'),
    path('permissions/rejected/all/add',views.add,name='add'),
    
    path('permission/reject/<int:id>/',views.reject_permission,name='reject'),
    path('permission/unreject/<int:id>/',views.unreject_permission,name='unreject'),
#reset password
     path('password_reset/', views.password_reset, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    ##employee attendance
    path('record_attendance',views.record_attendance,name='record_attendance'),
]


