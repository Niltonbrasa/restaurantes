import unittest
from mcp_server.tools.order_tools import create_order, mock_orders_db

class TestOrderTools(unittest.TestCase):

    def setUp(self):
        # Clear mock_orders_db before each test if necessary, or ensure unique order IDs
        mock_orders_db.clear()

    def test_create_order_success(self):
        customer_data = {"phone": "test_customer_123", "name": "Test Customer"}
        items = [{"item_id": "item_1", "quantity": 1}, {"item_id": "item_3", "quantity": 2}]
        result = create_order(customer_data, items)

        self.assertTrue(result["success"])
        self.assertIn("order_id", result)
        self.assertIn(result["order_id"], mock_orders_db)
        self.assertEqual(mock_orders_db[result["order_id"]]["customer_phone"], customer_data["phone"])
        self.assertEqual(len(mock_orders_db[result["order_id"]]["items_json"]), len(items))
        # A more precise total_amount check would require knowing item_1 and item_3 prices used in create_order
        # For now, just check it's a float.
        self.assertIsInstance(result["order_details"]["total_amount"], float)


    def test_create_order_fail_no_phone(self):
        customer_data = {"name": "No Phone Customer"}
        items = [{"item_id": "item_1", "quantity": 1}]
        result = create_order(customer_data, items)
        self.assertFalse(result["success"])
        self.assertIn("error", result)

    def test_create_order_fail_no_items(self):
        customer_data = {"phone": "test_customer_456"}
        items = []
        result = create_order(customer_data, items)
        self.assertFalse(result["success"])
        self.assertIn("error", result)

    def test_create_order_fail_invalid_item_format(self):
        customer_data = {"phone": "test_customer_789"}
        items = [{"id": "item_1", "qty": 1}] # Incorrect keys
        result = create_order(customer_data, items)
        self.assertFalse(result["success"])
        self.assertIn("error", result)


if __name__ == '__main__':
    unittest.main()
