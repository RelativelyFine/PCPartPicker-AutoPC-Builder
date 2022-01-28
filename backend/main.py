from pcpartpicker import API


class Components:
    def __init__(self, region='ca'):
        self.api = API(region)
