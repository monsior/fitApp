from django.test import TestCase
from .models import Weight
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class WeightModelTests(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='user1')

    def test_is_weight_object_created(self):
        """
        check if weight object is created
        """
        w = Weight()
        w.weight = 73.5
        w.date = timezone.now()
        w.username = self.u
        w.save()
        self.assertEqual(w, Weight.objects.last())

    def tearDown(self):
        self.u.delete()
