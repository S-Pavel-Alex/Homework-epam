from homework6.task1 import instances_counter


@instances_counter
class User:
    pass


def test_positive_count_instance_get_create():
    assert User.get_created_instances() == 0
    user1, user2, user3 = User(), User(), User()
    assert user1.get_created_instances() == 3
    assert user2.get_created_instances() == 3
    assert user3.get_created_instances() == 3
    assert User.get_created_instances() == 3
    User.reset_instances_counter()


def test_positive_count_instance_reset_instance():
    user1, user2, user3 = User(), User(), User()
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
    assert user1.get_created_instances() == 0
    assert user2.get_created_instances() == 0
    assert user3.get_created_instances() == 0


def test_positive_with_inheritance():
    class User2(User):
        pass

    user = User()
    assert user.get_created_instances() == 1
    assert User.get_created_instances() == 1
    user2 = User2()
    assert User.get_created_instances() == 1
    assert user2.get_created_instances() == 1
    assert User2.get_created_instances() == 1
