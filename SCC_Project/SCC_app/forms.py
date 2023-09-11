from django import forms
from django.forms import ModelForm
from .models import Guest, Staff

# Checkin form
class CheckinForm(ModelForm):
    class Meta():
        model = Guest
        fields = ('provider_name', 'client', 'signed_out_by')
        labels = {
            'provider_name': 'Provider Name',
            'client':'Client Name',
            'signed_out_by':'Expected Party To Pick Up'
        }
        widgets = {
            'provider_name':forms.TextInput(attrs={'class':'form-control','id': 'validationCustom05', 'required': 'required'}),
            'client': forms.TextInput(attrs={'class':'form-control'}),
            'signed_out_by':forms.TextInput(attrs={'class':'form-control'}),

            
        }
    def clean_signed_out_by(self):
        signed_out_by = self.cleaned_data.get('signed_out_by')
        if signed_out_by and len(signed_out_by.strip()) < 2:
            raise forms.ValidationError("Expected pick up is required.")
        return signed_out_by
    def clean_provider_name(self):
        provider_name = self.cleaned_data.get('provider_name')
        if provider_name and len(provider_name.strip()) < 2:
            raise forms.ValidationError("Provider name is required.")
        return provider_name
    
    def clean_client(self):
        client = self.cleaned_data.get('client')
        if client and len(client.strip()) < 2:
            raise forms.ValidationError("Client name is required.")
        return client
    
    









class StaffForm(forms.ModelForm):
    class Meta():
        model = Staff
        fields = ('first_name', 'last_name', 'username', 'password')
        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'password': '',

        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}),
            # 'password_confirmation':forms.PasswordInput(attrs={'class':'form-control'})
        }
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name.strip()) < 2:
            raise forms.ValidationError("First name is required.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and len(last_name.strip()) < 2:
            raise forms.ValidationError("Last name is required.")
        return last_name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username.strip()) < 2:
            raise forms.ValidationError("Username is required.")
        if Staff.objects.filter(username=username).exists():
            raise forms.ValidationError("User already exists, please login.")
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password.strip()) < 8:
            raise forms.ValidationError("Password must be atleast 8 characters long.")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = self.data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation', "Passwords don't match.")

        return cleaned_data

class UpdateStaffForm(forms.ModelForm):
    class Meta():
        model = Staff
        fields = ('first_name', 'last_name', 'username', 'password')
        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'password': '',

        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}),
    
        }
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name.strip()) < 2:
            raise forms.ValidationError("First name is required.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and len(last_name.strip()) < 2:
            raise forms.ValidationError("Last name is required.")
        return last_name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username.strip()) < 2:
            raise forms.ValidationError("Username is required.")
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password.strip()) < 8:
            raise forms.ValidationError("Password must be atleast 8 characters long.")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = self.data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation', "Passwords don't match.")

        return cleaned_data

class SignOutForm(ModelForm):
    class Meta():
        model = Guest
        fields = ('provider_name', 'client', 'signed_out_by' )

        labels = {
            'signed_out_by': 'Responsible party for pick up',
            'client': 'Client Name',
            'provider_name': 'Signed-in'

        }
        
        widgets = {

            'signed_out_by': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Responsible Party Signing Out'}),
            'client':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clients Name', 'readonly':True}),
            'provider_name': forms.TextInput(attrs={'class':'form-control', 'readonly':True})
        }



    def clean_signed_out_by(self):
        signed_out_by = self.cleaned_data.get('signed_out_by')
        if signed_out_by and len(signed_out_by.strip()) < 2:
            raise forms.ValidationError("Expected pick up is required.")
        return signed_out_by
    def clean_provider_name(self):
        provider_name = self.cleaned_data.get('provider_name')
        if provider_name and len(provider_name.strip()) < 2:
            raise forms.ValidationError("Provider name is required.")
        return provider_name
    
    def clean_client(self):
        client = self.cleaned_data.get('client')
        if client and len(client.strip()) < 2:
            raise forms.ValidationError("Client name is required.")
        return client
    

class SearchForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name':'start_date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name':'end_date'}))
    searched = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'type': 'search',
            'placeholder': 'Search Clients',
            'aria-label': 'Search'
        })
    )






