from mcp_server.core_logic.tool_decorator import mcp_tool

# Mock database for menu items
mock_menu_db = {
    "item_1": {"id": "item_1", "name": "Cheeseburger", "description": "Classic beef cheeseburger", "price": 10.99, "category": "burgers", "available": True},
    "item_2": {"id": "item_2", "name": "Veggie Burger", "description": "Plant-based patty burger", "price": 11.99, "category": "burgers", "available": True},
    "item_3": {"id": "item_3", "name": "Fries", "description": "Crispy golden fries", "price": 3.99, "category": "sides", "available": True},
    "item_4": {"id": "item_4", "name": "Soda", "description": "Refreshing soft drink", "price": 1.99, "category": "drinks", "available": False}, # Example of unavailable item
    "item_5": {"id": "item_5", "name": "Salad", "description": "Fresh garden salad", "price": 7.99, "category": "salads", "available": True},
}

@mcp_tool
def get_menu_items(category: str = None, available_only: bool = True):
    """
    Retrieves menu items, optionally filtered by category and availability.
    Returns mock data.
    """
    items = []
    for item_id, item_data in mock_menu_db.items():
        if category and item_data["category"] != category:
            continue
        if available_only and not item_data["available"]:
            continue
        items.append(item_data)
    return items

@mcp_tool
def check_item_availability(item_id: str):
    """
    Checks if a specific menu item is available.
    Returns mock data.
    """
    item = mock_menu_db.get(item_id)
    if item:
        return {"item_id": item_id, "name": item["name"], "available": item["available"]}
    return {"item_id": item_id, "available": False, "error": "Item not found"}

@mcp_tool
def get_item_details(item_id: str):
    """
    Retrieves details for a specific menu item.
    Returns mock data.
    """
    item = mock_menu_db.get(item_id)
    if item:
        return item
    return {"item_id": item_id, "error": "Item not found"}

# Example usage (for testing purposes, will be removed or moved to tests later)
if __name__ == '__main__':
    print("All available items:", get_menu_items())
    print("\nBurgers:", get_menu_items(category="burgers"))
    print("\nAll items (including unavailable):", get_menu_items(available_only=False))
    print("\nAvailability of item_1:", check_item_availability("item_1"))
    print("\nAvailability of item_4:", check_item_availability("item_4"))
    print("\nAvailability of unknown_item:", check_item_availability("unknown_item"))
    print("\nDetails of item_2:", get_item_details("item_2"))
    print("\nDetails of unknown_item:", get_item_details("unknown_item"))
