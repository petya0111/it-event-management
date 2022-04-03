class IdGeneratorInt:
    def __init__(self):
        self.nextId = 0

    def get_next_id(self):
        self.nextId += 1
        return self.nextId
