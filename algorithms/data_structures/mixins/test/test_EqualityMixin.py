import unittest
from algorithms.data_structures.mixins.EqualityMixin import EqualityMixin


class TestEqualityMixin(unittest.TestCase):
    def test_same_types(self):
        class SameType(EqualityMixin):
            pass

        obj1 = SameType()
        obj2 = SameType()
        self.assertEqual(obj1, obj2)

        obj2.new_attr = 3
        self.assertNotEqual(obj1, obj2)

    def test_different_types(self):
        class SameType(EqualityMixin):
            pass

        class DiffType(EqualityMixin):
            pass

        obj1 = SameType()
        obj2 = DiffType()
        self.assertNotEqual(obj1, obj2)
