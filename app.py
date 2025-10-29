# Install FastMCP first:
# pip install fastmcp
# fastmcp run fastmcpdemo.py --transport streamable-http --host 0.0.0.0 --port 8000

import json
from agent_framework import TextContent
from fastapi.responses import JSONResponse
from fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("main")


# def serialize_for_mcp(obj):
#     if isinstance(obj, TextContent):
#         return obj.text
#     if hasattr(obj, "to_dict"):
#         return obj.to_dict()
#     return str(obj)

@mcp.tool(name="secret", description="get the secret value")
def get_secret() -> str:
    """Get the secret value."""
    secret_value = "mustang"
    print(f"Retrieving secret: {secret_value}")
    return JSONResponse(content={"secret": secret_value})

@mcp.tool(name="car", description="get a cool car")
def get_cars() -> str:
    """Get a cool car."""
    car = "68 mustang"
    print(f"Retrieving car: {car}")
    return json.dumps({"content": car})
    return car

# # Define a simple tool
# @mcp.tool(name="add", description="Add two numbers")
# def add(a: int, b: int) -> int:
#     """Add two integers and return the result."""
#     print(f"Adding {a} and {b}")
#     return JSONResponse(content={"result": a + b})
#     #return TextContent(f"The result is {a + b}")
#     #return a + b

# # Another example tool: calculate days between two dates
# @mcp.tool(name="calculate_days_between", description="Calculate days between two dates")
# def calculate_days_between(date1: str, date2: str) -> int:
#     """
#     Calculate the number of days between two dates in YYYY-MM-DD format.
#     """
#     print(f"56 Calculating days between {date1} and {date2}")
#     return 45
#     return str("56 days")
#     return {"result": "56 days"}

#     return JSONResponse(content={"result": "56 days"})
#     #return JSONResponse 56 days
#     return {"days": 56}

    
#     return TextContent("56 days")
#     import pandas as pd
#     d1 = pd.to_datetime(date1)
#     d2 = pd.to_datetime(date2)
#     #return the results in json format
#     return {"days": abs((d2 - d1).days)}

if __name__ == "__main__":
    # Run the server (default transport is STDIO)
    #mcp.run()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, path="/mcp")