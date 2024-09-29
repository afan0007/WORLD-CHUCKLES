from django.test import TestCase
from django.urls import reverse
from Users.models import *  # If you need to query models during tests

# Create your tests here.
class HomeViewTests(TestCase):
    def test_home_view_renders_correct_template(self):
        response = self.client.get(reverse('home'))  # Make an HTTP GET request
        self.assertEqual(response.status_code, 200)  # Check if the response is 200 OK
        self.assertTemplateUsed(response, 'home.html')  # Ensure the right template is used
    
    def test_home_view_displays_correct_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to the Homepage')  # Check if the content is displayed

