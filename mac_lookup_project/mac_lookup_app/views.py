from django.shortcuts import render
import csv
import os
import re
from .forms import MacAddressForm


def format_mac_address(mac_address):
    """Format MAC address to remove special characters and make it uppercase."""
    formatted_mac = mac_address.upper().replace("-", "").replace(":", "")
    return formatted_mac[:6] if len(formatted_mac) >= 6 else None


def validate_mac_address(mac_address):
    """Validate MAC address format using a regular expression."""
    mac_regex = re.compile(r"^([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2}$")
    return mac_regex.match(mac_address) is not None


def search_csv(file_path, search_value):
    """Search for the MAC address in the CSV file."""
    if not os.path.isfile(file_path):
        return None

    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if row["Assignment"] == search_value:
                    return (
                        row["Registry"],
                        row["Organization Name"],
                        row["Organization Address"],
                    )
    except IOError:
        return None


def mac_lookup(request):
    result = None
    error_message = None  # Initialize error_message

    if request.method == "POST":
        form = MacAddressForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data["mac_address"]

            # Check if the MAC address is valid
            if validate_mac_address(user_input):
                search_value = format_mac_address(user_input)

                # Check length after formatting
                if len(search_value) != 6:
                    error_message = (
                        "MAC address must contain exactly 12 hexadecimal digits."
                    )
                else:
                    file_path = "oui.csv"
                    result = search_csv(file_path, search_value)

                    if result is None:
                        error_message = "MAC address not found in the database."
            else:
                error_message = "Invalid MAC address format. Please use the format XX-XX-XX-XX-XX-XX or XX:XX:XX:XX:XX:XX"
        else:
            error_message = "Invalid form submission."

    else:
        form = MacAddressForm()

    return render(
        request,
        "lookup/index.html",  # Update the template name if required
        {
            "form": form,
            "result": result,
            "error_message": error_message,
        },
    )


def subnetting(request):
    return render(request, "lookup/subnetting.html")  # Render subnetting template


def dashboard(request):
    return render(request, "lookup/dashboard.html")
