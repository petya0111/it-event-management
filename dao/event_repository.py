from dao.json_repository import JsonRepository
from dao.id_generator_uuid import IdGeneratorUuid


class EventRepository(JsonRepository):
    def __init__(self):
        super().__init__(IdGeneratorUuid(),'output_json_db/events_db.json')
