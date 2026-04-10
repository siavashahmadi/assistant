"""
Wrapper for google-workspace-mcp that fixes the broken entry point.
The package does asyncio.run(mcp.run()), but FastMCP's run() is now
synchronous (calls anyio.run internally), so asyncio.run() gets None
and crashes. This wrapper calls mcp.run() directly.
"""
from google_workspace_mcp import config  # noqa: F401
from google_workspace_mcp.app import mcp

from google_workspace_mcp.prompts import calendar as calendar_prompts  # noqa: F401
from google_workspace_mcp.prompts import drive as drive_prompts  # noqa: F401
from google_workspace_mcp.prompts import gmail as gmail_prompts  # noqa: F401
from google_workspace_mcp.prompts import slides as slides_prompts  # noqa: F401
from google_workspace_mcp.resources import calendar as calendar_resources  # noqa: F401
from google_workspace_mcp.resources import drive as drive_resources  # noqa: F401
from google_workspace_mcp.resources import gmail as gmail_resources  # noqa: F401
from google_workspace_mcp.resources import sheets_resources  # noqa: F401
from google_workspace_mcp.resources import slides as slides_resources  # noqa: F401
from google_workspace_mcp.tools import calendar as calendar_tools  # noqa: F401
from google_workspace_mcp.tools import docs_tools, sheets_tools  # noqa: F401
from google_workspace_mcp.tools import drive as drive_tools  # noqa: F401
from google_workspace_mcp.tools import gmail as gmail_tools  # noqa: F401
from google_workspace_mcp.tools import slides as slides_tools  # noqa: F401

if __name__ == "__main__":
    mcp.run()
