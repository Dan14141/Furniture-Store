import re

from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ]
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ]
    )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        # Удаляем все нецифровые символы (пробелы, скобки, дефисы)
        cleaned_phone = re.sub(r'\D', '', data)

        if not cleaned_phone.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")

        # Проверяем длину номера (10 цифр для России без +7)
        if len(cleaned_phone) not in [10, 11]:
            raise forms.ValidationError("Неверная длина номера телефона. Должно быть 10 или 11 цифр")

        return cleaned_phone

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.strip():
            raise forms.ValidationError("Имя обязательно для заполнения")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.strip():
            raise forms.ValidationError("Фамилия обязательна для заполнения")
        return data