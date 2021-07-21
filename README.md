# loadtest_setup
> Load test setup with containerized Locust, Prometheus and Grafana


This project demonstrates how we can perform a load test with [locust](https://locust.io/), scrape the results via [locust_exporter](https://github.com/ContainerSolutions/locust_exporter) into Prometheus and display them on Grafana.

This project is heavily insprired by [this](https://blog.container-solutions.com/how-to-move-metrics-from-locust.io-to-grafana-via-prometheus) blog post by [ContainerSolutions](https://github.com/ContainerSolutions).
The `locust_exporter` and Grafana dashboard are directly taken from the blog post itself. This project tries to put them all into a single `docker-compose` file which can run them at once.

I have modified the dashboard JSON to tweak a few things, remove unwanted panels, some cosmetic changes here and there. Feel free to modify the same as per your requirements. You can find the JSON at [`grafana/dashboard.json`](grafana/dashboard.json).

## Data flow
> We have kept all the ports as default ones, for ease of use. You can change them as per your convenience, in their respective config files.
1. Locust starts on port `8089` and sends stats on the `/stats/requests` endpoint.
2. `locust_exporter` scrapes this endpoint, converts the stats into a format that is understood by Prometheus and pushes them on port `9646`
3. Prometheus listens on this port (that's what we configure in [`prometheus/loadtest.yaml`](prometheus/loadtest.yaml)) and pushes its metris to port `9090`
4. Next, we configure Prometheus as datasource in Grafana ([`grafana/provisioning/datasources/prom.yaml`](grafana/provisioning/datasources/prom.yaml)) to read from port `9090`.
5. Lastly, we configure dashboard in Grafana (in [`grafana/provisioning/dashboards/loadtest.yaml`](grafana/provisioning/dashboards/loadtest.yaml`)).

## Instructions
1. Make sure your script is ready to be executed. It should be named as `locustfile.py` and must be present in the same directory as the `docker_compose.yml`
    1. If you want to run a different file, you can make changes the the `docker_compose.yml`.

Refer the tree structure below:
```
.
├── docker-compose.yml
├── grafana
│   ├── dashboard.json
│   └── provisioning
│       ├── dashboards
│       │   └── loadtest.yaml
│       └── datasources
│           └── prom.yaml
├── LICENSE
├── locustfile.py
├── prometheus
│   └── loadtest.yaml
├── requirements.py
└── setup.cfg
```

2. Build and run services using `docker-compose up`
3. Go to `localhost:8089`, enter the number of concurrent users, the spawn rate, the host, and begin.
    1. Alternately, you can also run locust in [`headless`](https://docs.locust.io/en/stable/running-locust-without-web-ui.html#running-locust-without-the-web-ui) mode and just look at the Grafana dashboard in the next step.

![locsut_start_page.png](images/locsut_start_page.png?raw=True "locsut_start_page")

4. Go to `localhost:3000` to view your Grafana dashboard.

![grafana_dashboard.png](images/grafana_dashboard.png?raw=True "grafana_dashboard")

