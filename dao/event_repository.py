from dao.json_repository import JsonRepository


class EventRepository(JsonRepository):
    def __init__(self, id_generator, file_name):
        super().__init__(id_generator, file_name)
