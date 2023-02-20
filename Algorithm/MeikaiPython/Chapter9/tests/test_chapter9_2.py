import src.chapter9_2 as sut


class TestChapter9_2:
    def test_empty(self):
        binary_tree = sut.BinarySearchTree()
        assert binary_tree.root is None
        assert binary_tree.search(1) is None

    def test_add(self):
        binary_tree = sut.BinarySearchTree()
        assert binary_tree.add(6, 6) is True
        assert binary_tree.add(2, 2) is True
        assert binary_tree.add(7, 7) is True
        assert binary_tree.add(4, 4) is True
        assert binary_tree.add(1, 1) is True
        assert binary_tree.add(6, 6) is False
        assert binary_tree.add(1, 1) is False

        assert binary_tree.root == sut.Node(0, 6)
        assert binary_tree.search(6) == 6
        assert binary_tree.search(2) == 2
        assert binary_tree.search(7) == 7
        assert binary_tree.search(4) == 4
        assert binary_tree.search(1) == 1

        binary_tree.dump()

    def test_remove(self):
        binary_tree = sut.BinarySearchTree()
        binary_tree.add(6, 6)
        binary_tree.add(2, 2)
        binary_tree.add(7, 7)
        binary_tree.add(4, 4)
        binary_tree.add(1, 1)

        assert binary_tree.remove(1) is True
        assert binary_tree.remove(7) is True
        assert binary_tree.remove(6) is True
        assert binary_tree.remove(3) is False

        binary_tree.dump()

    def test_min_max_key(self):
        binary_tree = sut.BinarySearchTree()
        assert binary_tree.root is None
        assert binary_tree.min_key() is None
        assert binary_tree.max_key() is None

        binary_tree.add(6, 6)
        binary_tree.add(2, 2)
        assert binary_tree.min_key() == 2
        assert binary_tree.max_key() == 6

        binary_tree.add(7, 7)
        binary_tree.add(4, 4)
        binary_tree.add(1, 1)
        assert binary_tree.min_key() == 1
        assert binary_tree.max_key() == 7
