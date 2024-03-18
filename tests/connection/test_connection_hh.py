import pytest


def test_connect_to_api(service):
    assert service.connect_to_api() == 200


@pytest.mark.parametrize(
    "param",
    [
        "Python developer",
        "Менеджер",
        "Сантехник",
        "asd1234ads"
    ]
)
def test_get_vacancies(service, param):
    assert service.get_vacancies(param)
