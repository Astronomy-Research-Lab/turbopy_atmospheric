from turbopy import Simulation, Diagnostic

class ProjectileDiagnostic(Diagnostic):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        self.data = None
        self.component = input_data.get("component", 1)
        self.output_function = None
        self.csv = None
        
    def inspect_resource(self, resource):
        pass

    def diagnose(self):
        pass
        
    def initialize(self):
        pass
        
    def finalize(self):
        pass
        
    def print_diagnose(self, data):
        print(data)

    def csv_diagnose(self, data):
        self.csv.append(data)