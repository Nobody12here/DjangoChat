from django import forms
from .models import Profile, User


class ProfileForm(forms.ModelForm):
    """Form definition for Sign Up."""

    class Meta:
        """Meta definition for SignUpform."""

        model = Profile
        
        fields = ["profile_picture"]


class CustomUserForm(forms.ModelForm):
    """Form definition for CustomUser."""

    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        """Meta definition for CustomUserform."""

        model = User
        fields = ("first_name", "last_name", "email", "password", "confirm_password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 "
                    "text-gray-900 dark:text-white text-sm rounded-lg block w-full p-2.5"
                }
            )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password and confirm password are different!")
        return cleaned_data

    def save(self, commit=True):
        user: User = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
