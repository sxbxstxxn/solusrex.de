from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Solusrex Sebastian Christoph")
        self.assertContains(response, "/static/css/main")
        self.assertContains(response, "/static/img/logo")
