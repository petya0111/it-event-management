from entity.group import Group
from entity.event import Event, EventStatusName, EventPost, EventInvitation, InvitationResponseTypeName
from entity.user import RoleName, User
from datetime import datetime

from service.event_service import EventService
from service.group_service import GroupService
from service.user_service import UserService
from dao.id_generator_uuid import IdGeneratorUuid


def print_repo_entity(repo):
    for p in repo:
        print(p.get_formatted_str())


if __name__ == '__main__':
    id_gen = IdGeneratorUuid()
    user_service = UserService()
    event_service = EventService()
    group_service = GroupService()

    python_devs = Group(name="Python", description="Python Group", user_ids=[], event_ids=[])

    admin11 = User(first_name='Maria', last_name='Georgieva', email="ivo@abc.bg", password="Test123",
                   bio="Passionate Python Dev",
                   is_active=True,
                   role=RoleName.ADMIN, group=python_devs)
    host1 = User(first_name='Ivan', last_name='Petrov', email="ivo@abc.bg", password="Test123",
                 bio="Passionate Python Dev", is_active=True,
                 role=RoleName.HOST, group=python_devs)
    guest1 = User(first_name='Dimitar', last_name='Hristov', email="dimitar@abc.bg", password="Test123",
                  bio="Backend Dev", is_active=True,
                  role=RoleName.GUEST, group=python_devs)

    users = [admin11, guest1, host1]
    for u in users:
        user_service.create(u)
    print("---Users---")
    print_repo_entity(user_service)

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
                                 event_status=EventStatusName(EventStatusName.OPEN_FOR_REGISTRATIONS),
                                 registered_user_ids=[])

    event_service.create_event_from_host(host1, python_latest_trends)
    event_service.add_event_post(python_latest_trends.id, EventPost(event_id=python_latest_trends.id,
                                                                    text="Registrate to our new latest event for python",
                                                                    creation_date=datetime.fromisoformat(
                                                                        '2022-01-22T10:30:00'),
                                                                    creation_user=host1.id))
    event_service.send_event_invitation(python_latest_trends.id,
                                        EventInvitation(event_id=python_latest_trends.id, user_id=guest1.id,
                                                        sent_date=datetime.fromisoformat(
                                                            '2022-01-23T10:30:00')))
    python_group = Group("Python", "python user group of professionals", [guest1.id], [python_latest_trends.id])
    group_service.create(python_group)
    group_service.allow_event_in_group(python_latest_trends.id, python_group.id)
    allowed: bool = group_service.check_event_allowed_group(str(python_group.id), str(python_latest_trends.id))
    print("Allowed event for group: ", allowed)

    print("--- Events -----")
    print_repo_entity(event_service)

    print("---Groups---")
    print_repo_entity(group_service)
    # user responds invitation
    event_service.respond_event_invitation(event_id=python_latest_trends.id, text_response="Many thanks I will participate for sure",
                                           response_date=datetime.fromisoformat('2022-01-24T10:30:00'),invitation_response=InvitationResponseTypeName.ACCEPT)
    # guest registers to event
    event_service.register_for_event(event=python_latest_trends, user=guest1,paid_date=datetime.fromisoformat('2022-01-24T12:30:00'),is_paid=False)
    event_service.save()
    group_service.save()
    user_service.save()

    # user_service.load()
    # group_service.load()
    # event_service.load()
    # print('\n', 'After Loading:')
    # print_repo_entity(user_service.find_all())
    # print_repo_entity(event_service.find_all())
    # print_repo_entity(user_service.find_all())
