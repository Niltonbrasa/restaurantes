# MCP Server
from mcp_server.tools import db_menu_tools, customer_tools, order_tools
from mcp_server.core_logic.tool_decorator import mcp_tool # Though not used directly here, good to show its context

# A simple way to "register" tools for now
# In a real MCP server, this would be more sophisticated,
# potentially involving dynamic loading, schema generation, etc.
REGISTERED_TOOLS = {
    # Database & Menu Tools
    "get_menu_items": db_menu_tools.get_menu_items,
    "check_item_availability": db_menu_tools.check_item_availability,
    "get_item_details": db_menu_tools.get_item_details,

    # Customer Intelligence Tools
    "get_customer_profile": customer_tools.get_customer_profile,
    "get_order_history": customer_tools.get_order_history,

    # Order & Delivery Tools
    "create_order": order_tools.create_order,

    # Future tools would be added here
}

def list_available_tools():
    """Returns a list of names of the available MCP tools."""
    return list(REGISTERED_TOOLS.keys())

def call_mcp_tool(tool_name: str, *args, **kwargs):
    """
    Calls a registered MCP tool by its name.
    This is a simplified dispatcher. A real implementation would handle
    errors more robustly, manage context, etc.
    """
    if tool_name not in REGISTERED_TOOLS:
        return {"error": f"Tool '{tool_name}' not found."}

    tool_function = REGISTERED_TOOLS[tool_name]
    try:
        # The @mcp_tool decorator already prints a message,
        # so we don't need extra print here if using the decorator.
        result = tool_function(*args, **kwargs)
        return result
    except Exception as e:
        # Basic error handling
        return {"error": f"Error executing tool '{tool_name}': {str(e)}"}

def main():
    print("MCP Server starting...")
    print("Registered MCP tools:")
    for tool_name in list_available_tools():
        print(f"- {tool_name}")

    print("\n--- Example Tool Calls ---")

    # Example: Get all available menu items
    print("\nCalling get_menu_items (all available):")
    menu_items_result = call_mcp_tool("get_menu_items", available_only=True)
    print("Result:", menu_items_result)

    # Example: Get customer profile
    print("\nCalling get_customer_profile (for '1234567890'):")
    profile_result = call_mcp_tool("get_customer_profile", phone="1234567890")
    print("Result:", profile_result)

    # Example: Create an order
    print("\nCalling create_order:")
    order_result = call_mcp_tool(
        "create_order",
        customer_data={"phone": "new_customer_123", "name": "Test Customer"},
        items=[{"item_id": "item_1", "quantity": 1}]
    )
    print("Result:", order_result)

    # Example: Call a non-existent tool
    print("\nCalling a non_existent_tool:")
    error_result = call_mcp_tool("non_existent_tool")
    print("Result:", error_result)

if __name__ == "__main__":
    main()
