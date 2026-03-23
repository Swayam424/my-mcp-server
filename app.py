from fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware  # <--- Make sure this is there!
import os

# 1. Initialize the MCP Server
mcp = FastMCP("MyFirstServer")

# 2. Add CORS Middleware (The "Universal Key")
mcp.app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all websites/apps to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Your Samosa Tool
@mcp.tool()
def get_favorite_snack(name: str) -> str:
    """A tool that predicts your favorite snack."""
    return f"I've analyzed the data, {name}. You definitely enjoy Samosas!"

# 4. Start command for Render
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
