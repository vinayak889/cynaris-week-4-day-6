from django.test import SimpleTestCase, Client


class AppSmokeTests(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CI/CD Demo App")

    def test_health_endpoint(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
