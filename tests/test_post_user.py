from src.services import UserApiService


def test_can_get_list_users(faker):
    user = {
        "name": faker.name(),
        "job": "leader"
    }

    response = UserApiService().create_user(user)

    assert response.status_code(201)
    assert response.field('name') == user['name']
