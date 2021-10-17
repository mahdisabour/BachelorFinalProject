
class CustomJsonExtraction:
    def __init__(self, model, exclude_fields) -> None:
        self.model = model
        self.exclude_fields = exclude_fields

    def get_fields(self):
        return [f.name for f in self.model._meta.get_fields()]

    def extract_data(self, json):
        model_fields = self.get_fields()
        json_fields = json
        print(json_fields)
        print(type(json_fields))
        extracted_data = {
            key: val for key, val in json_fields.items() if (key in model_fields) and (key not in self.exclude_fields)
        }
        return extracted_data