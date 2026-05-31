from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_homepage_renders(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Solusrex Sebastian Christoph")
        self.assertContains(response, "/static/css/main")
        self.assertContains(response, "/static/img/logo")
        self.assertContains(response, "Verlag")
        self.assertContains(response, "Shops")
        self.assertContains(response, "Impressum")

    def test_content_pages_render(self):
        for route_name, title in (
            ("verlag", "Verlag"),
            ("shops", "Shops"),
            ("impressum", "Impressum"),
        ):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f"<h1>{title}</h1>", html=True)
                self.assertContains(response, "Impressum")
