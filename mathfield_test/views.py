from django.views.generic import ListView

from mathfield_test import models as mathfield_test_models


class MathfieldListView(ListView):
    model = mathfield_test_models.MathfieldTest
