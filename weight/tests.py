from django.test import TestCase
from .models import Weight


class WeightModelTests(TestCase):

    def test_is_weight_positive(self):
        """
        weight value should be positive
        """