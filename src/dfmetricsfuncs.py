import os
import requests

class dfmetrics:
    def __init__(self, logging):
        self.logging = logging
        self.form_inventory_api_url = os.getenv('FORM_INVENTORY_API_URL', 'http://localhost:5000/api/v1/forms/statistics')

    def genFormInventoryMetrics(self):
        self.logging.info("Generating metrics for form inventory")
        try:
            response = requests.get(self.form_inventory_api_url)
            data = response.json()
            return data
        except Exception as e:
            self.logging.error("Error in generating metrics for form inventory")
            self.logging.info(e)
            return []

    def genAvailableFormsMetric(self, form_type):
        inventory = self.genFormInventoryMetrics()
        for item in inventory:
            if item['form_type'] == form_type:
                return item['available_forms']
        return 0

    def genLeasedFormsMetric(self, form_type):
        inventory = self.genFormInventoryMetrics()
        for item in inventory:
            if item['form_type'] == form_type:
                return item['leased_forms']
        return 0

    def genTotalFormsMetric(self, form_type):
        inventory = self.genFormInventoryMetrics()
        for item in inventory:
            if item['form_type'] == form_type:
                return item['total_forms']
        return 0

    def genTotalUsedFormsMetric(self, form_type):
        inventory = self.genFormInventoryMetrics()
        for item in inventory:
            if item['form_type'] == form_type:
                return item['total_used_forms']
        return 0