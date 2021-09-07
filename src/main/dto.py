class DatabaseDTO():
    def __init__(self, **kwargs):
        self.database = kwargs['database']
        self.last_results = kwargs['last_results']
        status_int = self.last_results.count()
        self.count = self.last_results.count()
        for result in self.last_results:
            if result.colour == "orange":
                status_int -= 0.5
            elif result.colour == "red":
                status_int -= 1

        self.status = "Впорядке"
        if status_int <= self.last_results.count() // 2:
            self.status = "Сбои"

