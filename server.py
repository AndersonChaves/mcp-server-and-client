import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route, Mount
 
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
 
from tools import get_rain_15min_from_location
 
mcp = FastMCP("weather-prediction")
 
@mcp.tool()
def tool_get_rain_15min_from_location(location:str):    
    """
    Returns the amount of rainfall recorded in the last 15 minutes for a given location (neighborhood)
    in Rio de Janeiro, using the city's public weather API.
 
    Parameters:
        location (str): The name of the neighborhood in Rio de Janeiro to query rainfall data for.
 
    Returns:
        float: The amount of rain in millimeters (mm) recorded in the last 15 minutes
               at the specified location.
 
    Example:
        >>> tool_get_rain_15min_from_location("Guaratiba")
        0.0
 
    Notes:
        - If the neighborhood is not found in the API data, an error may be raised or a null value returned.
        - This tool fetches real-time weather data from:
          https://api.dados.rio/v2/clima_pluviometro/precipitacao_15min/
    """
    return get_rain_15min_from_location(location)
 
sse = SseServerTransport("/messages/")
 
async def handle_sse(request: Request) -> None:
    _server = mcp._mcp_server
    async with sse.connect_sse(
        request.scope,
        request.receive,
        request._send,
    ) as (reader, writer):
        await _server.run(
            reader, writer, _server.create_initialization_options()
        )
 
# Create two endpoints
app = Starlette(
    debug=True,
    routes=[
        Route("/sse", endpoint=handle_sse),
        Mount("/messages/", app=sse.handle_post_message),
    ],
)
 
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
