import unittest
from mcp_server.server import call_mcp_tool, list_available_tools, REGISTERED_TOOLS

class TestMCPServer(unittest.TestCase):

    def test_list_available_tools(self):
        tool_list = list_available_tools()
        self.assertIsInstance(tool_list, list)
        self.assertEqual(len(tool_list), len(REGISTERED_TOOLS))
        for tool_name in REGISTERED_TOOLS.keys():
            self.assertIn(tool_name, tool_list)

    def test_call_mcp_tool_get_menu_items(self):
        # This tests the dispatcher and the underlying tool indirectly
        result = call_mcp_tool("get_menu_items", category="burgers", available_only=True)
        self.assertNotIn("error", result)
        self.assertIsInstance(result, list)
        if result: # If any burgers are returned
            self.assertTrue(all(item.get('category') == "burgers" and item.get('available') for item in result))

    def test_call_mcp_tool_get_customer_profile(self):
        result = call_mcp_tool("get_customer_profile", phone="1234567890") # known mock phone
        self.assertNotIn("error", result)
        self.assertEqual(result.get("phone"), "1234567890")

    def test_call_mcp_tool_create_order(self):
        customer_data = {"phone": "server_test_customer", "name": "Server Test"}
        items = [{"item_id": "item_2", "quantity": 1}]
        result = call_mcp_tool("create_order", customer_data=customer_data, items=items)
        self.assertTrue(result.get("success"))
        self.assertIn("order_id", result)

    def test_call_mcp_tool_not_found(self):
        result = call_mcp_tool("non_existent_tool_for_testing")
        self.assertIn("error", result)
        self.assertTrue("not found" in result["error"].lower())

    def test_call_mcp_tool_with_tool_error(self):
        # To test this properly, we might need a mock tool that reliably errors
        # or rely on a tool that can error, e.g., create_order with bad input
        result = call_mcp_tool("create_order", customer_data={}, items=[]) # Missing phone, should error
        self.assertFalse(result.get("success")) # The tool itself returns success:False
        self.assertIn("error", result)


if __name__ == '__main__':
    unittest.main()
