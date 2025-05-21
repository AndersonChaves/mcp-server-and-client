import streamlit as st
import asyncio
import traceback
from mcp import ClientSession
from mcp.client.sse import sse_client
from llm import invoke_llm
 
estacoes = ["Guaratiba", "Flamengo", "Vila Valqueire", "Urca", "Rocha Miranda"]
  
def main():
    st.title("Está chovendo no Rio?")
    st.write("Faça uma pergunta para checar os dados climáticos no Rio de Janeiro usando servidor MCP.")
    st.write(f"Estações disponíveis: {estacoes}")
 
    server_url = st.text_input("MCP Server URL", "http://localhost:8001/sse")
    question = st.text_input("Pergunta", "Está chovendo em Guaratiba?")
 
    if st.button("Checar"):
        neighbourhood = neighborhood_for_rain_check(question)
        if neighbourhood == "unrelated":
            answer = invoke_llm([question])
            st.info(f"{answer}")
        else:
            st.info("Consultando MCP server para verificar chuva...")
            try:            
                weather_data = asyncio.run(call_weather_tool(server_url, neighbourhood))
                prompt = question + " Considere os seguintes dados da API do Alerta RIO: " + \
                                weather_data.content[0].text
                answer = invoke_llm([prompt])
                st.subheader(f"Chuva em {neighbourhood}")                    
                st.success(answer)                    
            except Exception as e:
                st.error(f"Erro ocorrido: {e}")
 
def neighborhood_for_rain_check(question: str) -> str:
    prompt = "Cheque se esta pergunta está fazendo uma pergunta relacionada a chuva " \
    "ou meteorologia. Se não, responda com a palavra unrelated, e nada mais. " \
    "Se estiver, responda com o nome da localidade questionada. Siga os exemplos:" \
    "<Example output 1> Guaratiba" \
    "<Example output 1> Flamengo" \
    "<Example output 1> Vila Valqueire" \
    "<Example output 1> unrelated"
    answer = invoke_llm([prompt, question])
    return answer.lower()
 
async def call_weather_tool(server_url: str, location: str):
    """
    Connects to the MCP server using SSE, initializes the session,
    calls the tool_summarize_url tool, and returns the result.
    """
    try:
        async with sse_client(server_url) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                print_items("tools", await session.list_tools())
                result = await session.call_tool("tool_get_rain_15min_from_location", arguments={"location": location})
                return result
           
    except Exception as e:
        return f"Error: {e}\n{traceback.format_exc()}"
 
def print_items(name: str, result) -> None:
    print(f"Tool disponível: {name}:")
    items = getattr(result, name)
    if items:
        for item in items:
            print(" *", item)
    else:
        print("Não há tools disponíveis")
 
if __name__ == "__main__":
    main()