import requests
from requests.exceptions import RequestException
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS
 
def get_rain_15min_from_location(location: str) -> float:
    url = 'https://api.dados.rio/v2/clima_pluviometro/precipitacao_15min/'
    headers = {
        'accept': 'application/json',
        'X-CSRFToken': 'ibFOs7hegrzFacvltgYQvkU5h82K7gnpmzu6v3ncqttIcYsdPCmBCcIYrpvVYRXG'
    }
 
    try:
        response = requests.get(url, headers=headers)
 
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar a API: {response.status_code} - {response.text}")
 
        data = response.json()
 
        for estacao in data:
            if estacao.get("bairro", "").lower() == location.lower():
                return estacao                
 
        raise ValueError(f"Bairro '{location}' não encontrado na resposta da API.")
    except ValueError as e:
        raise McpError(ErrorData(INVALID_PARAMS, str(e))) from e
    except RequestException as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Request error: {str(e)}")) from e
    except Exception as e:
        raise McpError(ErrorData(INTERNAL_ERROR, f"Unexpected error: {str(e)}")) from e