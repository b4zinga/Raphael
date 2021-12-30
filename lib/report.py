# author: myc

import time
import json


class Report:
    def __init__(self):
        self.content = ""
        self.time = time.strftime("%Y-%m-%d %H:%M:%S")

    def _build_html_report(self, ret_queue):
        html_report = "<b>Raphael Report at: {}</b>".format(self.time)
        html_report += "<table border='1'>\n"
        html_report += "<tr bgcolor='#87CEFA'><th>Host</th><th>Plugin</th><th>Result</th></tr>\n"
        while not ret_queue.empty():
            host, plugin, result = ret_queue.get()
            html_report += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(host, plugin, result)
        html_report += "</table>"
        return html_report

    def _build_json_report(self, ret_queue):
        json_report = "\nRaphael Report at: {}\n".format(self.time)
        while not ret_queue.empty():
            host, plugin, result = ret_queue.get()
            r = {"host":host, "plugin":plugin, "result":result}
            json_report += json.dumps(r, sort_keys=True, indent=4, separators=(',', ': '))
        return json_report

    def _build_csv_report(self, ret_queue):
        csv_report = "\nRaphael Report at: {}\n".format(self.time)
        csv_report += "Host,plugin,result,\n"
        while not ret_queue.empty():
            host, plugin, result = ret_queue.get()
            csv_report += "{},{},{}\n".format(host, plugin, result)
        return csv_report

    def build_report(self, ret_queue, fmt="html"):
        if fmt == "html":
            self.content = self._build_html_report(ret_queue)
        elif fmt == "json":
            self.content = self._build_json_report(ret_queue)
        elif fmt == "csv":
            self.content = self._build_csv_report(ret_queue)

    def save_report(self, path):
        file = open(path, "a")
        file.write(self.content)
        file.close()
