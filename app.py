from fastmcp import FastMCP
import os

# 1. Initialize the MCP Server
# We give it a name and tell it exactly how to behave
mcp = FastMCP("MyFirstServer")

# 2. Add your tool
@mcp.tool()
def get_favorite_snack(name: str) -> str:
    """A tool that predicts your favorite snack."""
    return f"I've analyzed the data, {name}. You definitely enjoy Samosas!"

# 3. The Render Start Command
if __name__ == "__main__":
    # Render uses port 10000 by default often, but we check the environment variable
    port = int(os.getenv("PORT", 10000))
    # We use host 0.0.0.0 so the internet can see it
    mcp.run(transport="sse", host="0.0.0.0", port=port)
