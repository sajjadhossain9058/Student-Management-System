from django import forms
from core.models import Students
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]
        labels = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "username":"Username"
        }
    
    def clean_email(self):
        email = self.cleaned_data.get("email","").strip().lower()
        if User.objects.filter(email__iexact = email).exists():
            raise forms.ValidationError("The email is already exist. Try another one")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # password1/password2 are declared on UserCreationForm,
        # so their labels must be set here, not in Meta.labels.
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["sid","name","email","department","batch","image"]
        labels = {
            "sid":"Student ID",
            "name":"Name",
            "email":"Email",
            "department":"Department",
            "batch":"Batch",
            "image":"Image"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing an existing student, don't allow the ID to be changed
        if self.instance and self.instance.pk:
            self.fields["sid"].disabled = True