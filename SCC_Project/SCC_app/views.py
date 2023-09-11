from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CheckinForm, StaffForm, SignOutForm, SearchForm, UpdateStaffForm
from .models import Guest, Staff
from django.db.models import Q

import bcrypt


# Landing Page to sign clients in    
def UserCheck_in_page(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)  # Create an instance of CheckinForm

        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            messages.success(request, "User Successfully Checked-in")
            return redirect("/serenity/check_in/guest")
        else:
            # Form is not valid, handle error case
            messages.error(request, "Please correct the errors below.")

    else:
        form = CheckinForm()

    context = {'form': form}
    return render(request, 'checkin.html', context)

# Clients that are currently signed-in
def Signed_In_Clients(request):
    context = {
        'all_guest': Guest.objects.all(),
    }
    return render(request, 'signed_in_clients.html', context)

# Form for the provider to sign the client out
def sign_out_client(request, guest_id):
    provider = Guest.objects.get(id=guest_id)
    
    if request.method == 'POST':
        form = SignOutForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('/serenity/check_in/guest')
    else:
        form = SignOutForm(instance=provider)
    
    return render(request, 'sign-out.html', {'form': form, 'provider': provider})



# This page has a table that conatins the providers name, client name, signed-in by, signed-out by, with date & time
# renders after login
def AllCheckedInUsers(request):
    if 'staff_id' not in request.session:
        return redirect('/serenity/check_in/guest')
    staff = Staff.objects.get(id = request.session['staff_id'])
    context = {
        'all_guest': Guest.objects.all(),
        'staff':staff,
    }
    return render(request,"checked_in_users.html", context)


# Form used to create new staff memebers
def CreateStaffPage(request):
    # if 'staff_id' not in request.session:
    #     return redirect('/serenity/staff/login/')
    
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            # Form data is valid, create the staff account
            pwd = form.cleaned_data['password']
            pw_hash = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
            Staff.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=pw_hash
            )
            messages.success(request, "Account Creation Successful")
            return redirect('/serenity/new/staff')
    else:
        form = StaffForm()

    context = {'form': form}
    return render(request, 'create_staff.html', context)

    
# Login form for staff members
def staff_login_form(request):
    staff = Staff.objects.filter(username=request.POST['username'])
    if staff:
        logged_staff = staff[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged_staff.password.encode()):
            request.session['staff_id'] = logged_staff.id

            return redirect('/serenity/checked_in/users/')
    messages.error(request, "Incorrect Username or Password.")
    return redirect('/serenity/staff/login/')

# staff login page
def StaffLoginPage(request):
    return render(request, 'staff_login.html')

# Search bar form, used to search for clients and the dates they came into the office
def search_clients(request):
    if 'staff_id' not in request.session:
        return redirect('/serenity/staff/login/')        
    
    if request.method == "POST":
        if 'searched' in request.POST:
            form = SearchForm(request.POST)
            searched = request.POST['searched']
        if form.is_valid():
            searched = form.cleaned_data['searched']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            clients = Guest.objects.filter(Q(provider_name__icontains=searched) | Q(client__icontains=searched), created_at__date__range = [start_date, end_date])
            return render(request, 'checked_in_users.html', {'searched':searched, 'clients': clients })
        else:
            return redirect("/serenity/checked_in/users")
    else:
        form = SearchForm()
        return render(request, 'checked_in_users.html', {'form':form})

    
# Page thats shows all staff members
def AllStaff(request):
    if 'staff_id' not in request.session:
        return redirect('/serenity/staff/login/')

    context = {
        'all_staff': Staff.objects.all()
    }
    return render(request, 'all_staff.html', context )

# Update staff
def UpdateStaff(request, staff_id):
    if 'staff_id' not in request.session:
        return redirect('/serenity/staff/login/')
    
    staff = get_object_or_404(Staff, id=staff_id)
    
    if request.method == 'POST':
        form = UpdateStaffForm(request.POST, instance=staff)
        
        if form.is_valid():
            # Get the password from the form
            password = form.cleaned_data['password']
            
            # Hash the password
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
            # Update staff member's information
            staff = form.save(commit=False)
            staff.password = pw_hash  # Update the hashed password
            staff.save()
            
            messages.success(request, "Account updated successfully")
            return redirect(f'/serenity/edit/staff/{staff_id}/')
    else:
        form = UpdateStaffForm(instance=staff)

    return render(request, 'update_staff.html', {'form': form, 'staff': staff})
        




# Delete staff
def DeleteStaff(request, staff_id):
    if 'staff_id' not in request.session:
        return redirect('/serenity/staff/login/')
    
    staff = Staff.objects.get(pk = staff_id)
    staff.delete()
    return redirect('/serenity/staff/')

# Logout for staff members
def logout_view(request):
    if 'staff_id' not in request.session:
        return redirect('/serenity/staff/login/')
    logout(request)

    return redirect('/serenity/check_in/guest/')