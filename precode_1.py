import pytest

from miles import HobbitsPriorityStatus

class TestHobbitsPriorityStatus:

    @pytest.mark.parametrize(
        'hobbit, priority_status',
        [
            ['Фродо', 'Platinum'],
            ['Сэм', 'Gold'],
            ['Мерри', 'Silver'],
            ['Пиппин', 'Silver'],
        ]
    )
    def test_priority_status(self, hobbit, priority_status):
        assert HobbitsPriorityStatus().get_status(hobbit) == priority_status
