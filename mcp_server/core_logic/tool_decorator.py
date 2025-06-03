import functools

def mcp_tool(func):
    """
    A decorator to mark a function as an MCP tool.
    In the future, this can be expanded to register tools,
    handle schemas, etc.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # For now, it just calls the original function.
        # Future enhancements:
        # - Register the tool with a central registry.
        # - Validate input/output against a schema.
        # - Add logging or monitoring.
        print(f"Calling MCP tool: {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
