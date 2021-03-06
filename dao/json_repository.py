import json

from dao.repository import Repository


class JsonRepository(Repository):
    def __init__(self, id_generator, db_filename):
        super().__init__(id_generator)
        self.db_filename = db_filename

    def save(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            json.dump(list(self.find_all()), f, indent=4, default=dumper)

    def load(self):
        self.clear()
        with open(self.db_filename, "rt", encoding="utf-8") as f:
            entities = json.load(f, object_hook=object_hook)
            self.add_all(entities)


# Helpers
def dumper(obj):
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


def object_hook(jsdict):
    entity_module_name = jsdict['_module']
    entity_class_name = jsdict['_class']
    module = __import__(entity_module_name, fromlist=[entity_class_name])
    cls = getattr(module, entity_class_name)
    if hasattr(cls, 'from_json'):
        return cls.from_json(jsdict)
    obj = cls()
    obj.__dict__ = jsdict
    return obj
