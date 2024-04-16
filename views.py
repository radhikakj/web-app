from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EmployeeForm
from django.contrib import messages

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('employee_ID')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:  # Check if the user is an admin
                login(request, user)
                return redirect('admin_dashboard')  # Redirect admin to admin panel
            else:
                login(request, user)
                return redirect('employee_dashboard')  # Redirect regular user to their dashboard
        else:
            # Handle invalid login
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html', {'error_message': 'Invalid login'})
            
    else:
        return render(request, 'login.html')
    
    
def signup(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        employee_id = request.POST.get('employee_ID')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        phone = request.POST.get('contact_number')
        date_of_birth = request.POST.get('dob')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        country = request.POST.get('country')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')

        # Check if passwords match
        if password != cpassword:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Check if a user with the provided employee ID already exists
        if UserProfile.objects.filter(employee_id=employee_id).exists():
            return render(request, 'signup.html', {'error_message': 'User with this Employee ID already exists'})

        # Create a new user instance
        user = User.objects.create_user(username=employee_id, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name

        # Save the user to the database
        user.save()

        # Create a UserProfile instance and save user profile information
        profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            employee_id=employee_id,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            department=department,
            designation=designation,
            country=country,
            state=state,
            pin_code=pin_code
        )

        # Authenticate the newly created user
        user = authenticate(request, username=employee_id, password=password)

        # If the user is authenticated, log them in
        if user is not None:
            login(request, user)

            # Redirect superusers to admin panel
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')

        # Redirect to login page if signup is successful but authentication fails
        return redirect('')
    else:
        # If the request method is GET, render the signup form
        return render(request, 'signup.html')
def admin_dashboard(request):
    return render(request,'admin.html')
@login_required
def employee_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    return render(request,'employee_dashboard.html',{'user_profile': user_profile})
## ADMIN DASHBOARD
def employee_details(request):
    # Retrieve all user profiles
    user_profiles = UserProfile.objects.all()
    return render(request, 'employee-details.html', {'user_profiles': user_profiles})

def attendance_details(request):
    # Retrieve all user profiles
    user_profiles = UserProfile.objects.all()
    return render(request, 'attendance-details.html', {'user_profiles': user_profiles})
from .utils import get_all_months
# views.py
from django.shortcuts import render
import datetime

import datetime  # Import the datetime module

#def display_months(request):
    # Create a list of month names
    #months = [
        #'January', 'February', 'March', 'April', 'May', 'June',
       # 'July', 'August', 'September', 'October', 'November', 'December'
    #]

    # Alternatively, you can use list comprehension to generate month names
    # months = [datetime.date(1900, month, 1).strftime('%B') for month in range(1, 13)]

    #return render(request, 'view_month.html', {'months': months})
from flask import Flask
import calendar

app = Flask(__name__)

#@app.route('/')
def display_months(request):
    # Create a list to store data for all months
    months_data = []

    # Iterate over all months (1 to 12)
    for month in range(1, 13):
        # Get the number of days in the month
        num_days = calendar.monthrange(2024, month)[1]
        
        # Create a list to store dates for this month
        month_dates = []
        
        # Append all dates in the month to the list
        for day in range(1, num_days + 1):
            month_dates.append(f"2024-{month:02d}-{day:02d}")
        
        # Append the month data to the main list
        months_data.append({
            'name': calendar.month_name[month],  # Month name
            'dates': month_dates  # List of dates in the month
        })

    # Render the template with the months_data
    return render(request,'view_month.html', {'month_dates':months_data})

if __name__ == '__main__':
    app.run(debug=True)



def view_employee(request, id):
    user_profiles = UserProfile.objects.get(pk=id)
    return render(request, 'view_employee.html', {'user_profiles': user_profiles})
def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_f_name = form.cleaned_data['f_name'] 
            new_date_of_birth = form.cleaned_data['date_of_birth']
            new_bg = form.cleaned_data['bg']
            new_emergency_contact_no= form.cleaned_data['emergency_contact_no']  
            new_employee_id = form.cleaned_data['employee_id']
            
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']
            new_department = form.cleaned_data['department']
            new_designation = form.cleaned_data['designation']
            
            new_date_of_joining = form.cleaned_data['date_of_joining']
            new_address = form.cleaned_data['address']
            new_country = form.cleaned_data['country']
            new_state = form.cleaned_data['state']
            new_pin_code = form.cleaned_data['pin_code']
            new_gender = form.cleaned_data['gender']
            
            new_employee = UserProfile(
                first_name=new_first_name,
                last_name=new_last_name,
                f_name=new_f_name,
                date_of_birth=new_date_of_birth,
                bg=new_bg,
                emergency_contact_no=new_emergency_contact_no,
                employee_id=new_employee_id,
                email=new_email,
                phone=new_phone,
                department=new_department,
                designation=new_designation,
                date_of_joining=new_date_of_joining,
                address=new_address,
                country=new_country,
                state=new_state,
                pin_code=new_pin_code,
                gender=new_gender
            )
            
            new_employee.save()
            return render(request, 'add.html', {
                'form': EmployeeForm(),
                'success': True
            })
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {
        'form': form
    })


def edit(request, id):
    if request.method == 'POST':
        employee = UserProfile.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        employee = UserProfile.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {
        'form': form
    })
def delete(request, id):
    # Get the employee object or return a 404 error page if it doesn't exist
    employee = get_object_or_404(UserProfile, pk=id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the employee
        employee.delete()
        # Redirect to a specific URL after deletion, adjust as needed
        return redirect('employee-details')
    
    # Pass the employee object to the template context for rendering
    return render(request, 'delete.html', {'employee': employee})
    


from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile  # Import the UserProfile model

def attend_delete(request, id):
    # Get the employee object or return a 404 error page if it doesn't exist
    employee = get_object_or_404(UserProfile, pk=id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the employee
        Attendance.delete()
        # Redirect to a specific URL after deletion, adjust as needed
        return redirect('attendance-details')
    
    # Pass the employee object to the template context for rendering
    return render(request, 'attend_delete.html', {'employee': employee})

def month_delete(request):
    # Get the employee object or return a 404 error page if it doesn't exist
    employee = get_object_or_404(UserProfile, pk=id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the employee
        employee.delete()
        # Redirect to a specific URL after deletion, adjust as needed
        return redirect('view-month')
    
    # Pass the employee object to the template context for rendering
    return render(request, 'month_delete.html', {'employee': employee})
    
    

def leave(request):
    return render(request,'leave.html')

def request(request):
    return render(request,'request.html')
def permission(request):
    return render(request,'permission.html')
## EMPLOYEE PROFILES

def attendance(request):
    employee = UserProfile.objects.get(user=request.user)
    current_date = timezone.now().strftime("%d-%m-%Y")
    return render(request,'attendance.html', {'employee': employee,'current_date': current_date})

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request,'profile.html',{'user_profile': user_profile})

def leave_request(request):
    return render(request,'leave_request.html')

def permission_request(request):
    return render(request,'permission_request.html')

def change_password(request):
    return render(request,'change_password.html')



# LEAVE REQUEST
from leave.models import Leave  # Replace "permission.models" with "leave.models"
from scientiaarc_app.models import UserProfile
from leave.forms import LeaveCreationForm  # Replace "permission.forms" with "leave.forms"
from leave.manager import LeaveManager  # Replace "permission.manager" with "leave.manager"
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Replace "permission" with "leave" in function names, variables, and imports

def leave_creation(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.method == 'POST':
		form = LeaveCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()


			# print(instance.defaultdays)
			messages.success(request,'Leave Request Sent,wait for Admins response',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('createleave')

		messages.error(request,'failed to Request a Leave,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('createleave')


	dataset = dict()
	form = LeaveCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'create_leave.html',dataset)
	

#finish





def leaves_list(request):
	if not (request.user.is_staff and request.user.is_superuser):
		return redirect('/')
	leaves = Leave.objects.all_pending_leaves()
	return render(request,'leaves_recent.html',{'leave_list':leaves,'title':'leaves list - pending'})

#finish

def leaves_approved_list(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	leaves = Leave.objects.all_approved_leaves() #approved leaves -> calling model manager method
	return render(request,'leaves_approved.html',{'leave_list':leaves,'title':'approved leave list'})



def leaves_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	leave = get_object_or_404(Leave, id = id)
	print(leave.user)
	employee = UserProfile.objects.filter(user = leave.user)[0]
	print(employee)
	return render(request,'leave_detail_view.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})









def approve_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	user = leave.user
	employee = UserProfile.objects.filter(user = user)[0]
	leave.approve_leave

	messages.error(request,'Leave successfully approved for {0}'.format(employee.first_name),extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('userleaveview', id = id)


def cancel_leaves_list(request):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leaves = Leave.objects.all_cancel_leaves()
	return render(request,'leaves_cancel.html',{'leave_list_cancel':leaves,'title':'Cancel leave list'})



def unapprove_leave(request,id):
	if not (request.user.is_authenticated and request.user.is_superuser):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.unapprove_leave
	return redirect('leaveslist') #redirect to unapproved list




def cancel_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.leaves_cancel

	messages.success(request,'Leave is rejected',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('canceleaveslist')#work on redirecting to instance leave - detail view


# Current section -> here
def uncancel_leave(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	leave = get_object_or_404(Leave, id = id)
	leave.status = 'pending'
	leave.is_approved = False
	leave.save()
	messages.success(request,'Leave is unrejected,now in pending list',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('canceleaveslist')#work on redirecting to instance leave - detail view



#def leave_rejected_list(request):

	#dataset = dict()
	#leave = Leave.objects.all_rejected_leaves()

	#dataset['leave_list_rejected'] = leave
	#return render(request,'rejected_leaves_list.html',dataset)



#def reject_leave(request,id):
	#if not (request.user.is_superuser and request.user.is_authenticated):
		#return redirect('/')
	#leave = get_object_or_404(Leave, id = id)
	#leave.leaves_cancel

	#messages.success(request,'Leave is canceled',extra_tags = 'alert alert-success alert-dismissible show')
	#return redirect('leaveslist')#work on redirecting to instance leave - detail view


	# return HttpResponse(id)


#def unreject_leave(request,id):
	#if not (request.user.is_authenticated and request.user.is_superuser):
		#return redirect('/')
	#leave = get_object_or_404(Leave, id = id)
	#leave.unreject_leave
	#return redirect('leaveslist') #redirect to unapproved list



#  staffs leaves table user only
def view_my_leave_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		leaves = Leave.objects.filter(user = user)
		employee = UserProfile.objects.filter(user = user).first()
		print(leaves)
		dataset = dict()
		dataset['leave_list'] = leaves
		dataset['employee'] = employee
		dataset['title'] = 'Leaves List'
	else:
		return redirect('login')
	return render(request,'staff_leaves_table.html',dataset)



#PERMISSION REQUEST

from permission.models import Permission
from scientiaarc_app.models import UserProfile
from permission.forms import PermissionCreationForm
from permission.manager import PermissionManager
from leave.models import Leave  # Replace "permission.models" with "leave.models"
from scientiaarc_app.models import UserProfile  # Replace "permission.forms" with "leave.forms"  # Replace "permission.manager" with "leave.manager"
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages



def permission_creation(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.method == 'POST':
		form = PermissionCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()


			# print(instance.defaultdays)
			messages.success(request,'Permission Request Sent,wait for Admins response',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('createpermission')

		messages.error(request,'failed to Request a Permission,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('createpermission')


	dataset = dict()
	form = PermissionCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Apply for Permission'
	return render(request,'create_permission.html',dataset)
	

#finish





def permission_list(request):
	if not (request.user.is_staff and request.user.is_superuser):
		return redirect('/')
	permissions = Permission.objects.all_pending_permissions()
	return render(request,'permission_recent.html',{'permission_list':permissions,'title':'permissions list - pending'})

#finish

def permissions_approved_list(request):
	if not (request.user.is_superuser and request.user.is_staff):
		return redirect('/')
	permissions = Permission.objects.all_approved_permissions() #approved leaves -> calling model manager method
	return render(request,'permissions_approved.html',{'permission_list':permissions,'title':'approved permission list'})



def permissions_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	permission = get_object_or_404(Permission, id = id)
	print(permission.user)
	employee = UserProfile.objects.filter(user = permission.user)[0]
	print(employee)
	return render(request,'permission_detail_view.html',{'permission':permission,'employee':employee,'title':'{0}-{1} permission'.format(permission.user.username,permission.status)})



#def approve_permission(request,id):
	#if not (request.user.is_superuser and request.user.is_authenticated):
		#return redirect('/')
	#permission = get_object_or_404(Permission, id = id)
	#user = permission.user
	#employee = UserProfile.objects.filter(user = user)[0]
	#permission.approve_permission

	#messages.error(request,'Permission successfully approved for {0}'.format(employee.first_name),extra_tags = 'alert alert-success alert-dismissible show')
	#return redirect('userpermissionview', id = id)


def cancel_permissions_list(request):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	permissions = Permission.objects.all_cancel_permissions()
	return render(request,'permissions_cancel.html',{'permission_list_cancel':permissions,'title':'Cancel permission list'})



#def unapprove_permission(request,id):
	#if not (request.user.is_authenticated and request.user.is_superuser):
		#return redirect('/')
	#permission = get_object_or_404(Permission, id = id)
	#permission.unapprove_permission
	#return redirect('permissionslist') #redirect to unapproved list




def cancel_permission(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	permission = get_object_or_404(Permission, id = id)
	permission.permission_cancel

	messages.success(request,'Permission is approved',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('cancelpermissionslist')#work on redirecting to instance leave - detail view


# Current section -> here
def uncancel_permission(request,id):
	if not (request.user.is_superuser and request.user.is_authenticated):
		return redirect('/')
	permission = get_object_or_404(Permission, id = id)
	permission.status = 'pending'
	permission.is_approved = False
	permission.save()
	messages.success(request,'Permission is unapproved,now in pending list',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('cancelpermissionslist')#work on redirecting to instance leave - detail view



def permission_rejected_list(request):

	dataset = dict()
	permission = Permission.objects.all_rejected_permissions()

	dataset['permission_list_rejected'] = permission
	return render(request,'rejected_permissions_list.html',dataset)



def reject_permission(request,id):
	dataset = dict()
	permission = get_object_or_404(Permission, id = id)
	permission.reject_permission
	messages.success(request,'Permission is rejected',extra_tags = 'alert alert-success alert-dismissible show')
	return redirect('permissionsrejected')

	# return HttpResponse(id)


def unreject_permission(request,id):
	permission = get_object_or_404(Permission, id = id)
	permission.status = 'pending'
	permission.is_approved = False
	permission.save()
	messages.success(request,'Permission is now in pending list ',extra_tags = 'alert alert-success alert-dismissible show')

	return redirect('permissionsrejected')



#  staffs leaves table user only
def view_my_permission_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		permissions = Permission.objects.filter(user = user)
		employee = UserProfile.objects.filter(user = user).first()
		print(permissions)
		dataset = dict()
		dataset['permission_list'] = permissions
		dataset['employee'] = employee
		dataset['title'] = 'Permissions List'
	else:
		return redirect('login')
	return render(request,'staff_permissions_table.html',dataset)





#Forget password

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

def password_reset(request):
    return render(request,'password_reset.html')

def view_my_leave_table(request):
	# work on the logics
	if request.user.is_authenticated:
		user = request.user
		leaves = Leave.objects.filter(user = user)
		employee = UserProfile.objects.filter(user = user).first()
		print(leaves)
		dataset = dict()
		dataset['leave_list'] = leaves
		dataset['employee'] = employee
		dataset['title'] = 'leaves List'
	else:
		return redirect('login')
	return render(request,'emp_leaves_table.html',dataset)

def view_my_permission_table(request):
	 #work on the logics
	if request.user.is_authenticated:
		user = request.user
		permissions = Permission.objects.filter(user = user)
		employee = UserProfile.objects.filter(user = user).first()
		print(permissions)
		dataset = dict()
		dataset['permission_list'] = permissions
		dataset['employee'] = employee
		dataset['title'] = 'Permissions List'
	else:
		return redirect('login')
	return render(request,'emp_permissions_table.html',dataset)


def empleaves_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	leave = get_object_or_404(Leave, id = id)
	print(leave.user)
	employee = UserProfile.objects.filter(user = leave.user)[0]
	print(employee)
	return render(request,'emp_leaves_table.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})

def emppermissions_view(request,id):
	if not (request.user.is_authenticated):
		return redirect('/')

	permission = get_object_or_404(Permission, id = id)
	print(permission.user)
	employee = UserProfile.objects.filter(user = permission.user)[0]
	print(employee)
	return render(request,'emp_permissions_table.html',{'permission':permission,'employee':employee,'title':'{0}-{1} permission'.format(permission.user.username,permission.status)})



#-----------------------------------------ATTENDANCE-----------------------------------------------------#

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from attendance.models import Attendance

@login_required
def forenoon_clock_in(request):
    today_attendance, created = Attendance.objects.get_or_create(user=request.user, date=timezone.now().date())
    if today_attendance.forenoon_clock_in:
        messages.error(request, "You have already clocked in for the forenoon shift.")
    else:
        today_attendance.forenoon_clock_in = timezone.now()
        today_attendance.save()
        messages.success(request, "Forenoon Clock in successful.")
    return redirect('attendance')

@login_required
def forenoon_clock_out(request):
    today_attendance, created = Attendance.objects.get_or_create(user=request.user, date=timezone.now().date())
    if today_attendance.forenoon_clock_out:
        messages.error(request, "You have already clocked out for the forenoon shift.")
    else:
        today_attendance.forenoon_clock_out = timezone.now()
        today_attendance.save()
        messages.success(request, "Forenoon Clock out successful.")
    return redirect('attendance')

@login_required
def afternoon_clock_in(request):
    today_attendance, created = Attendance.objects.get_or_create(user=request.user, date=timezone.now().date())
    if today_attendance.afternoon_clock_in:
        messages.error(request, "You have already clocked in for the afternoon shift.")
    else:
        today_attendance.afternoon_clock_in = timezone.now()
        today_attendance.save()
        messages.success(request, "Afternoon Clock in successful.")
    return redirect('attendance')

@login_required
def afternoon_clock_out(request):
    today_attendance, created = Attendance.objects.get_or_create(user=request.user, date=timezone.now().date())
    if today_attendance.afternoon_clock_out:
        messages.error(request, "You have already clocked out for the afternoon shift.")
    else:
        today_attendance.afternoon_clock_out = timezone.now()
        today_attendance.save()
        messages.success(request, "Afternoon Clock out successful.")
    return redirect('attendance')
# Implement similar views for forenoon_clock_out, afternoon_clock_in, and afternoon_clock_out

#@login_required
#def attendance_page(request):
    #today_attendance, created = Attendance.objects.get_or_create(user=request.user, date=timezone.now().date())
    #context = {'today_attendance': today_attendance}
    #return render(request, 'attendance.html', context)


# views.py

#### EMPLOYEE ATTENDANCE ####

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from attendance.models import Attendance
from django.http import JsonResponse
from datetime import datetime, time
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def record_attendance(request):
    if request.method == 'POST':
        button_clicked = request.POST.get('button_clicked')
        
        # Retrieve the user profile of the currently logged-in user
        user_profile = request.user.userprofile

        # Get the current time
        current_time = datetime.now().time()

        # Define the specific times for clock-in, break-in, break-out, and clock-out
        clock_in_time = time(9, 0)  # 9:00 AM
        clock_in_grace_time = time(9, 30)  # 9:30 AM
        before_noon_break_in_time = time(10, 50)  # 10:50 AM
        before_noon_break_out_time = time(11, 0)  # 11:00 AM
        before_noon_clock_out_time_female = time(12, 30)  # 12:30 PM
        before_noon_clock_out_time_male = time(13, 0)  # 1:00 PM
        afternoon_clock_in_time_female = time(13, 0)  # 1:00 PM
        afternoon_clock_in_time_male = time(13, 30)  # 1:30 PM
        afternoon_break_in_time = time(15, 50)  # 3:50 PM
        afternoon_break_out_time = time(16, 0)  # 4:00 PM
        afternoon_clock_out_time = time(17, 30)  # 5:30 PM
        afternoon_clock_out_time_leave = time(18, 0)  # 6:00 PM

        # Handle clock-in
        if button_clicked == 'morningClockIn':
            if current_time <= clock_in_grace_time:
                button_clicked = 'Clock In (On Time)'
            elif current_time <= before_noon_break_in_time:
                button_clicked = 'Clock In (Late)'
            else:
                button_clicked = 'Leave'

        # Handle break-in and break-out
        elif button_clicked in ['morningBreakIn', 'morningBreakOut']:
            if current_time >= before_noon_break_in_time and current_time <= before_noon_break_out_time:
                button_clicked = 'Break In / Break Out'
            else:
                button_clicked = 'Invalid'

        # Handle clock-out
        elif button_clicked == 'morningClockOut':
            if user_profile.gender == 'Female':
                if current_time <= before_noon_clock_out_time_female:
                    button_clicked = 'Clock Out (On Time)'
                else:
                    button_clicked = 'Leave'
            else:  # Male
                if current_time <= before_noon_clock_out_time_male:
                    button_clicked = 'Clock Out (On Time)'
                else:
                    button_clicked = 'Leave'

        # Handle afternoon clock-in
        elif button_clicked == 'afternoonClockIn':
            if current_time >= afternoon_clock_in_time_female:
                if user_profile.gender == 'Female':
                    button_clicked = 'Clock In (On Time)'
                else:
                    button_clicked = 'Clock In (Late)'
            elif current_time >= afternoon_clock_in_time_male:
                if user_profile.gender == 'Male':
                    button_clicked = 'Clock In (On Time)'
                else:
                    button_clicked = 'Clock In (Late)'
            else:
                button_clicked = 'Leave'

        # Handle afternoon break-in and break-out
        elif button_clicked in ['afternoonBreakIn', 'afternoonBreakOut']:
            if current_time >= afternoon_break_in_time and current_time <= afternoon_break_out_time:
                button_clicked = 'Break In / Break Out'
            else:
                button_clicked = 'Invalid'

        # Handle afternoon clock-out
        elif button_clicked == 'afternoonClockOut':
            if current_time <= afternoon_clock_out_time:
                button_clicked = 'Clock Out (On Time)'
            else:
                button_clicked = 'Clock Out (Late)'

        # Create an attendance record for the user
        Attendance.objects.create(user_profile=user_profile, button_clicked=button_clicked)
        
        # Return a success response
        return JsonResponse({'status': 'success', 'button_clicked': button_clicked})
    
    return JsonResponse({'status': 'error'})