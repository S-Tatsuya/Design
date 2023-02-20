import pytest

from src.chapter8_2 import Node, Linkedlist


class TestChapter8_2:
    def test_node(self):
        sut = Node(1)
        assert sut.data == 1
        assert sut.next is None

        test_data = Node(3)
        sut = Node(2, test_data)
        assert sut.data == 2
        assert sut.next == test_data

    def test_linked_list(self):
        sut = Linkedlist()

        assert sut.no == 0
        assert sut.head is None
        assert sut.current is None
        assert len(sut) == 0

        assert sut.search(3) == -1
        assert (3 in sut) is False

        sut.add_first(3)

        assert sut.search(3) == 0
        assert (3 in sut) is True
        assert len(sut) == 1

        sut.add_first(2)
        assert sut.search(2) == 0
        assert sut.search(3) == 1
        assert len(sut) == 2

        sut.add_last(5)
        assert sut.search(5) == 2
        assert len(sut) == 3

        sut.remove_first()
        assert sut.search(2) == -1
        assert len(sut) == 2

        sut.remove_last()
        assert sut.search(5) == -1
        assert len(sut) == 1

        sut.add_last(5)
        sut.add_first(2)
        assert len(sut) == 3

        assert sut.output_current_node() == 2
        sut.next()
        assert sut.output_current_node() == 3
        sut.remove_current_node()
        assert sut.search(3) == -1
        assert len(sut) == 2
        assert sut.output_current_node() == 2

        sut.clear()
        assert sut.search(2) == -1
        assert sut.search(5) == -1
        assert len(sut) == 0

    def test_linked_list_empty(self):
        sut = Linkedlist()
        sut.remove_first()

        assert len(sut) == 0

        sut.remove_last()
        assert len(sut) == 0

    def test_linked_list_iter(self):
        sut = Linkedlist()
        sut.add_first(5)
        sut.add_first(4)
        sut.add_first(3)
        sut.add_first(2)
        sut.add_first(1)

        iter = sut.__iter__()
        assert next(iter) == 1
        assert next(iter) == 2
        assert next(iter) == 3
        assert next(iter) == 4
        assert next(iter) == 5
        with pytest.raises(StopIteration) as e:
            next(iter)

        assert str(e.value) == ""
