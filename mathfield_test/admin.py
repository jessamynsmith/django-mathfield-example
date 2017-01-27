from django.contrib import admin
from django import forms
from mathfield.widgets import MathFieldWidget

from mathfield_test import models as mathfield_test_models


class MathfieldTestForm(forms.ModelForm):

    class Meta:
        widgets = {
            'latex': MathFieldWidget
        }


class MathfieldTestAdmin(admin.ModelAdmin):
    form = MathfieldTestForm


admin.site.register(mathfield_test_models.MathfieldTest, MathfieldTestAdmin)
