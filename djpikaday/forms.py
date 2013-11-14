from django.forms import DateField

from .widgets import PikadayInput


class PikadayField(DateField):
    widget = PikadayInput
