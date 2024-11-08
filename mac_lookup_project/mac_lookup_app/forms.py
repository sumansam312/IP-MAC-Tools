# mac_lookup_app/forms.py
from django import forms


class MacAddressForm(forms.Form):
    mac_address = forms.CharField(
        label="MAC Address",
        max_length=17,
        widget=forms.TextInput(attrs={"placeholder": "XX:XX:XX:XX:XX:XX"}),
    )
