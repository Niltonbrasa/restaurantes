import unittest
from mcp_server.tools.db_menu_tools import get_menu_items, check_item_availability, get_item_details, mock_menu_db

class TestDBMenuTools(unittest.TestCase):

    def test_get_menu_items_all_available(self):
        items = get_menu_items(available_only=True)
        self.assertTrue(all(item['available'] for item in items))
        self.assertEqual(len(items), len([item for item in mock_menu_db.values() if item['available']]))

    def test_get_menu_items_all_items(self):
        items = get_menu_items(available_only=False)
        self.assertEqual(len(items), len(mock_menu_db))

    def test_get_menu_items_by_category(self):
        items = get_menu_items(category="burgers")
        self.assertTrue(all(item['category'] == "burgers" for item in items))
        self.assertTrue(len(items) > 0)

    def test_check_item_availability_available(self):
        result = check_item_availability("item_1") # Assumes item_1 is available in mock_db
        self.assertTrue(result["available"])
        self.assertEqual(result["item_id"], "item_1")

    def test_check_item_availability_unavailable(self):
        result = check_item_availability("item_4") # Assumes item_4 is unavailable
        self.assertFalse(result["available"])
        self.assertEqual(result["item_id"], "item_4")

    def test_check_item_availability_not_found(self):
        result = check_item_availability("unknown_item")
        self.assertFalse(result["available"])
        self.assertIn("error", result)

    def test_get_item_details_found(self):
        details = get_item_details("item_1")
        self.assertEqual(details["id"], "item_1")
        self.assertEqual(details["name"], mock_menu_db["item_1"]["name"])

    def test_get_item_details_not_found(self):
        details = get_item_details("unknown_item")
        self.assertIn("error", details)

if __name__ == '__main__':
    unittest.main()
