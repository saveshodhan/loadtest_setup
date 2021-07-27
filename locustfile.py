"""Test project locustfile."""

from locust import constant, LoadTestShape, tag, task
from locust.contrib.fasthttp import FastHttpUser
from locust.log import setup_logging


setup_logging("DEBUG", None)


class TestProject(FastHttpUser):
    """Main locust class for test project."""

    host = "https://httpbin.org/"
    wait_time = constant(0)

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


# class SpikeShape(LoadTestShape):
#     """LoadTestShape for spikes."""

#     USER_COUNT = 100
#     SPAWN_RATE = 100
#     ON_INTERVAL = 20
#     OFF_INTERVAL = 10

#     def tick(self):
#         """Tick."""
#         run_time = self.get_run_time()
#         if (run_time // self.ON_INTERVAL) % 2 == 1 and (run_time // self.OFF_INTERVAL) % 2 == 0:
#             return (0, self.SPAWN_RATE)
#         return (self.USER_COUNT, self.SPAWN_RATE)
