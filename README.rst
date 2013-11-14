**Django Pikaday**

A simple app that provides easy integration with the Pikaday Datepicker.

MIT licensed

**Compatibility**

* Django 1.4, 1.5, 1.6
* Python 2.7, 3.x
* Browsers: Chrome, Firefox 3.5, IE8, Opera 10, Safari 3.2 and later

**Installation**

  .. code:: bash

   pip install django-pikaday

Or install directly from master branch:

  .. code:: bash

   pip install git+http://github.com/caioariede/django-pikaday.git#egg=django-pikaday==1.0

**Configuration**

Add :code:`djpikaday` to the :code:`INSTALLED_APPS` setting.

**Usage**

  .. code:: python

   from django import forms
   from djpikaday.widgets import PikadayInput

   class YourForm(forms.ModelForm):
       widgets = {
           'my_date_field': PikadayInput(),  # Uses DATE_FORMAT
       }

**Using a custom format**

  .. code:: python

   from django import forms
   from djpikaday.forms import PikadayField

   class YourForm(forms.ModelForm):
       # Needs to use the format described in:
       # http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
       widgets = {
           'my_date_field': PikadayInput(format='%Y-%m-%d'),
       }
