class DatabaseDTO():
    def __init__(self, **kwargs):
        self.database = kwargs['database']
        self.last_results = kwargs['last_results']
        self.status_int = 0
        self.count = self.last_results.count()
        for result in self.last_results:
            if result.colour == "#2fcc66":
                self.status_int += 1

        if self.last_results.count() != 0:
            self.status_int = self.status_int / self.last_results.count()

        self.last_results = reversed(kwargs['last_results'])
        self.status = "Впорядке"
        if self.status_int <= 0.5:
            self.status = "Сбои"
        self.status_int *= 100


class ParserDTO():
    def __init__(self, **kwargs):
        self.parser = kwargs['parser']
        self.last_reports = kwargs['last_reports']
        self.status_int = 0
        self.count = self.last_reports.count()
        for report in self.last_reports:
            if report.status == "ok":
                self.status_int += 1

        if self.last_reports.count() != 0:
            self.status_int = self.status_int / self.last_reports.count()

        self.last_results = reversed(kwargs['last_reports'])
        self.status = "Впорядке"
        if self.status_int <= 0.5:
            self.status = "Сбои"
        self.status_int *= 100
