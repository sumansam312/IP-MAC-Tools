# IP-MAC-Tools

Efficient and easy-to-use network management tools for calculating subnets and identifying devices by MAC address, accessible on both mobile and desktop browsers.

---

## Features

### Subnetting Tool:

- **Calculate Subnet Details:** Determine the network ID, broadcast address, usable IP range, total IPs, and more.
- **CIDR to IP Range Conversion:** Convert any given IP address and subnet mask into the complete list of IP addresses.
- **IP Classes:** Supports IP class determination (Class A, B, C).
- **Responsive Design:** Optimized for both mobile and desktop devices.

### MAC Address Lookup:

- **Search by MAC Address:** Identify device manufacturer details by submitting a MAC address.
- **Simple and Fast:** Get results instantly with user-friendly forms.
- **Comprehensive Results:** Displays details such as the organization name, address, and registry information associated with the MAC address.

---

## Installation Guide

### Prerequisites:

- **Python 3.8 or above**
- **pip** package manager (should be included with Python)
- **Django** (for web framework support)
- **Other dependencies** listed below in `requirements.txt`

### Steps to Install:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sumansam312/IP-MAC-Tools.git

   cd IP-MAC-Tools
   ```

2. **Create a virtual environment:**
   If you don't already have `virtualenv` installed, you can install it via:

   ```bash
   pip install virtualenv
   ```

   Then, create and activate the virtual environment:

   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   Install all the necessary dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate the database (if applicable):**
   This project uses Django, so you'll need to apply the migrations:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   Now, the app should be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser.

---

## How to Use

### Subnetting Tool:

1. **Enter an IP address** and **subnet mask** in CIDR format (e.g., `192.168.1.0/24`).
2. **Specify the number of IPs** you want to display (optional).
3. Click **Calculate** to see the subnet details and the full range of IP addresses in the subnet.

### MAC Address Lookup:

1. **Enter the MAC address** you want to search for (e.g., `00:1A:2B:3C:4D:5E`).
2. Click **Lookup** to find the manufacturer and other details associated with that MAC address.

---

## Requirements

This project uses the following Python libraries:

- **Django 3.0+**
- **python 3.8+**
- **requests**
- **re**
- **os**
- **csv**

These are listed in the `requirements.txt` file. You can install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix (git checkout -b feature-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to your branch (git push origin feature-name).
5. Create a new Pull Request.

---

## Acknowledgments

- Django Framework for building the web application.
- FontAwesome for the icons.
- Open Source Contributors for their support and contributions.

---

### Explanation of the Sections:

1. **Project Title**: The project name is the first heading, followed by a brief description of the project.
2. **Features**: Lists the primary functionalities of the application, including subnetting and MAC address lookup.
3. **Installation Guide**: Provides the steps to install the project, create a virtual environment, and install dependencies.
4. **How to Use**: Describes how users can interact with the application (subnetting and MAC lookup).
5. **Project Structure**: A visual directory structure of the project.
6. **Requirements**: Lists the required dependencies for running the project.
7. **License and Contributing**: Information about contributing to the project and the license (MIT).
8. **Acknowledgments**: A section where you credit frameworks or libraries used in your project.

---

### To Save:

- Copy the above content into a new file named `README.md` in the root of your project.

---
