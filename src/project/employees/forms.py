from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Employees, WorkingDays
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model, password_validation
from project.utils.slugify import slugify
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class EmployeeForm(forms.ModelForm):
    user_first_name = forms.CharField(label=_("First Name"), widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    user_last_name = forms.CharField(label=_("Last Name"), widget=forms.TextInput(attrs={"placeholder": "Last name"}))
    user_password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    user_email = forms.EmailField()
    user_group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Employees
        fields = [
            "user_first_name",
            "user_last_name",
            "user_password",
            "user_email",
            "user_group",
            "specialist_type",
            "working_days"
        ]
        widgets = {
            "working_days": forms.CheckboxSelectMultiple
        }

    def _post_clean(self):
        super()._post_clean()

        password = self.cleaned_data.get("user_password")

        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("user_password", error)

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            user = User.objects.create_user(
                username=slugify("{last_name}_{first_name}".format(
                    last_name=self.cleaned_data["user_last_name"],
                    first_name=self.cleaned_data["user_first_name"],
                )),
                first_name=self.cleaned_data["user_first_name"],
                last_name=self.cleaned_data["user_last_name"],
                email=self.cleaned_data["user_email"],
                password=self.cleaned_data["user_password"],
            )
            user.groups.add(self.cleaned_data["user_group"])

            instance.user = user
            instance.save()

            if hasattr(self, "save_m2m"):
                self.save_m2m()

        return instance
