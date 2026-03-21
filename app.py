from fastmcp import FastMCP

# 1. Initialize the MCP Server
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
    mcp.run(transport="sse")