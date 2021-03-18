from turbopy import Simulation, Diagnostic, CSVOutputUtility

class ProjectileDiagnostic(Diagnostic):
    def __init__(self, owner: Simulation, input_data: dict):
        super().__init__(owner, input_data)
        self.data = None
        self.component = input_data.get("component", 1)
        self.output_function = None
        self.csv = None
        
    def inspect_resource(self, resource):
        if "Projectile:" + self.component in resource:
            self.data = resource["Projectile:" + self.component]

    def diagnose(self):
        if self.data:
            self.output_function(self.data[0, :])
        
    def initialize(self):
        functions = {"stdout": self.print_diagnose,
                     "csv": self.csv_diagnose}
        self.output_function = functions[self._input_data["output_type"]]
        if self._input_data["output_type"] == "csv":
            diagnostic_size = (self._owner.clock.num_steps + 1, 3)
            self.csv = CSVOutputUtility(
                self._input_data["filename"],
                diagnostic_size)
        
    def finalize(self):
        self.diagnose()
        if self._input_data["output_type"] == "csv":
            self.csv.finalize()
        
    def print_diagnose(self, data):
        print(data)

    def csv_diagnose(self, data):
        self.csv.append(data)