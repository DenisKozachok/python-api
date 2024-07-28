from src.services import UserApiService


def test_can_get_list_users():
    response = UserApiService().get_users()

    assert response.status_code(200)
    print(response)


def test_can_get_user_by_id():
    response = UserApiService().get_user_by_id(1)

    assert response.status_code(200)
    print