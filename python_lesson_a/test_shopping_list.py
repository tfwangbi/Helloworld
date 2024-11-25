import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):

    def setUp(self):
        list1 = {"Apple": 50, "Orange": 30, "Purple": 45, "Banana": 40}
        self.shopping_list = ShoppingList(list1)

    def test_shopping_list_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 4)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 165)
