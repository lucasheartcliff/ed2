class Edge:
    source:any
    target: any
    weight: float
    def __init__(self, source, target, weight=1):
        self.source = source
        self.target= target
        self.weight= weight
