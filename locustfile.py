"""Test project locustfile."""

from locust import tag, task
from locust.contrib.fasthttp import FastHttpUser


class TestProject(FastHttpUser):
    """Main locust class for test project."""

    host = "https://httpbin.org/"

    @tag("2xx")
    @task(100)
    def run_2xx_codes(self):
        """Run for 2xx return codes."""
        for i in [200, 201, 204]:
            self.client.post(f"/status/{i}", name="2xx")

    @tag("5xx")
    @task
    def run_5xx_codes(self):
        """Run for 5xx return codes."""
        for i in [500, 502, 503]:
            self.client.post(f"/status/{i}", name="5xx")
