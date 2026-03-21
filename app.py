mcp = FastMCP("MyFirstServer")

# 2. Add a simple Tool
@mcp.tool()
def get_favorite_snack(name: str) -> str:
    """
    A simple tool that tells you what snack someone likes.
    """
    return f"I've checked my data, {name}. You look like someone who enjoys Samosas!"

# 3. This starts the server
if __name__ == "__main__":
   if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
