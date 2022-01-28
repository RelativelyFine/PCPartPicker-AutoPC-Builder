from pcpartpicker import API


class Components:
    def __init__(self, region='ca'):
        self.api = API(region)

    def get_component_json(self, component: str):
        component_data = self.api.retrieve(component)
        return component_data
