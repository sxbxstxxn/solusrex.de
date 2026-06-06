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

    def test_verlag_page_renders_book_tile(self):
        response = self.client.get(reverse("verlag"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Verlag</h1>", html=True)
        self.assertContains(response, "Nur ich und die Welt")
        self.assertContains(response, "Simon Ryberg")
        self.assertContains(response, "Weitere Titel folgen")
        self.assertContains(response, "Solusrex Verlag")
        self.assertContains(response, "Demnächst verfügbar")
        self.assertContains(response, "https://www.amazon.de/dp/B0H37M8CDG")
        self.assertContains(response, "/static/img/nur-ich-und-die-welt")
        self.assertNotContains(
            response,
            "Diese Inhalte werden derzeit redaktionell erarbeitet und stehen Ihnen in KÃ¼rze zur VerfÃ¼gung",
        )

    def test_content_pages_render(self):
        for route_name, title in (
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
                    "Diese Inhalte werden derzeit redaktionell erarbeitet und stehen Ihnen in Kürze zur Verfügung",
                )

    def test_impressum_page_is_removed(self):
        response = self.client.get("/impressum/")

        self.assertEqual(response.status_code, 404)
