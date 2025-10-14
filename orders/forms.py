import re

from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[("0", False),
                 ("1", True),])
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[("0", False),
                 ("1", True),])

    def clean_first_name(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Ваш номер должен содержать только цифры: '0123456789'")

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data