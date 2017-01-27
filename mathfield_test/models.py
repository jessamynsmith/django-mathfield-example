from django.db import models
from django.utils.safestring import mark_safe

from mathfield.models import MathField


class MathfieldTest(models.Model):
    latex = MathField()

    def __str__(self):
        return mark_safe(self.latex['html'])
