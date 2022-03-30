from dao.event_repository import EventRepository
from dao.group_repository import GroupRepository
from dao.user_repository import UserRepository
from entity.group import Group
from entity.event import Event, EventStatus, EventStatusName
from entity.user import RoleName, User
from datetime import  datetime
from utils.id_generator_uuid import IdGeneratorUuid


def print_repo_entity(repo):
    for p in repo:
        print(p.get_formatted_str())


if __name__ == '__main__':
    id_gen = IdGeneratorUuid()
    user_repo = UserRepository()
    event_repo = EventRepository()
    group_repo = GroupRepository()

    python_devs = Group(name="Python", description="Python Group", user_ids=[], event_ids=[])

    admin11 = User(first_name='Maria', last_name='Georgieva', email="ivo@abc.bg", bio="Passionate Python Dev",
                   is_active=True,
                   role=user_repo.create_role_for_user(RoleName.ADMIN), group=python_devs)
    host1 = User(first_name='Ivan', last_name='Petrov', email="ivo@abc.bg", bio="Passionate Python Dev", is_active=True,
                 role=user_repo.create_role_for_user(RoleName.HOST), group=python_devs)
    guest1 = User(first_name='Dimitar', last_name='Hristov', email="dimitar@abc.bg", bio="Backend Dev", is_active=True,
                  role=user_repo.create_role_for_user(RoleName.GUEST), group=python_devs)

    users = [admin11, guest1, host1]
    for u in users:
        user_repo.create(u)
    print("---Users---")
    print_repo_entity(user_repo)

    python_latest_trends = Event(name="Latest trends of pytthon", description="Get to know latest trends in clean code",
                                 creation_date=datetime.fromisoformat('2022-02-22T10:30:00'),
                                 registration_end_date=datetime.fromisoformat('2022-04-22T11:00:00'),
                                 start_datetime=datetime.fromisoformat('2022-04-22T10:30:00'),
                                 end_datetime=datetime.fromisoformat('2022-04-22T18:30:00'),
                                 place="Online",
                                 is_public=True,
                                 capacity=300,
                                 price=0,
                                 creation_user_id=host1.id,
                                 event_status=EventStatus(EventStatusName.OPEN_FOR_REGISTRATIONS),
                                 registered_user_ids=[])

    event_repo.create(python_latest_trends)

    python_group = Group("Python", "python user group of professionals", [guest1.id], [python_latest_trends.id])
    group_repo.create(python_group)
    group_repo.allow_event_in_group([str(python_latest_trends.id)], python_group.id)
    allowed: bool = group_repo.check_event_allowed_group(python_group.id,str(python_latest_trends.id))
    print("Allowed event for group: ", allowed)

    print("--- Events -----")
    print_repo_entity(event_repo)

    print("---Groups---")
    print_repo_entity(group_repo)

    event_repo.register_for_event(python_latest_trends, guest1)
