from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import Child,AdoptionRequest

class ChildModelTests(TestCase):
    def setUp(self):
        Child.objects.create(name="Test Child", age=5, description="Test description", gender="M")

    def test_child_creation(self):
        """Test if a child is created correctly"""
        child = Child.objects.get(name="Test Child")
        self.assertEqual(child.name, "Test Child")
        self.assertEqual(child.age, 5)
        self.assertEqual(child.description, "Test description")
        self.assertEqual(child.gender, "M")




class ChildListTests(TestCase):
    def test_adoption_request_page(self):
        """Test if the adoption request page loads correctly"""
        response = self.client.get(reverse('child_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Child List")



class ADonateTests(TestCase):
    def test_adoption_request_page(self):
        """Test if the adoption request page loads correctly"""
        response = self.client.get(reverse('donate'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Donate")

