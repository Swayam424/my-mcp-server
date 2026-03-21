from fastmcp import FastMCP  # <--- THIS IS THE MISSING LINE!
import os

# 1. Initialize the MCP Server
mcp = FastMCP("MyFirstServer")

# 2. Add a simple Tool
@mcp.tool()
def get_favorite_snack(name: str) -> str:
    """
    A simple tool that tells you what snack someone likes.
    """
    return f"I've checked my data, {name}. You look like someone who enjoys Samosas!"

# 3. This starts the server correctly for Render
if __name__ == "__main__":
    # Render provides a PORT environment variable automatically
    port = int(os.getenv("PORT", 8000))
    # '0.0.0.0' tells the server to listen to the internet
    mcp.run(transport="sse", host="0.0.0.0", port=port)
