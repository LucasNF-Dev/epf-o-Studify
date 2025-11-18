class Prova:
    def __init__(self, data, materia):

        self.data = data
        self.materia = materia 

        def to_dict(self):
            return{
                "data": self.data,
                "materia": self.materia
            }
        
        @staticmethod

        def from_dict(d):
            return Prova(d["data"], d["materia"])