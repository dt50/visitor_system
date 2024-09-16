from django import forms
from phonenumber_field.formfields import SplitPhoneNumberField

from .models import Visitor


class VisitorForm(forms.ModelForm):
    phone_number = SplitPhoneNumberField(initial="RU", required=False)
    class Meta:
        model = Visitor
        fields = ("fio", "phone_number", "mail", "address", "is_child", "children", "reason_for_request")
