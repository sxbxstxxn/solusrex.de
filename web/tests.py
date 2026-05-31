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
        self.assertContains(response, "c/o POSTFLEX PFX-796-792")

    def test_content_pages_render(self):
        for route_name, title in (
            ("verlag", "Verlag"),
            ("shops", "Shops"),
        ):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f"<h1>{title}</h1>", html=True)
                self.assertContains(response, "Sebastian Christoph")
                self.assertContains(response, "Emsdettener Straße 10")
                self.assertContains(
                    response,
                    "Inhalte noch nicht vorhanden. Sie folgen in Kürze.",
                )

    def test_impressum_page_is_removed(self):
        response = self.client.get("/impressum/")

        self.assertEqual(response.status_code, 404)
