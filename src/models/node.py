class Node :
    id: any
    data: dict[any,any]

    def __init__(self, id, data = {}):
        self.id = id
        self.data = data