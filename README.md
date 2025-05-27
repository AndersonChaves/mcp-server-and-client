# MCP Server Weather
 
Este projeto é uma implementação simples de um servidor que fornece informações meteorológicas usando o MCP (Model Context Protocol).
 
## Features
 
- Fornece dados meteorológicos para diferentes localidades.
- Implementa o protocolo MCP para comunicação.
- Leve e fácil de configurar
 
## Pré-requisitos
 
- [Python](https://www.python.org/) instalado no sistema.
- Conhecimento básico do protocolo MCP.
 
## Uso - Servidor
 
1. Inicie o servidor:
    ```bash
    python server.py
    ```
2. O servidor vai rodar em `http://localhost:8001` por padrão.
 
3. Use o cliente MCP para conectar rodar a consulta a dados climáticos.
 
4. Inicie a interface com o cliente:
    ```bash
    streamlit run client.py
    ```
5. Acesse a interface no navegador em `http://localhost:8501`.
 
Constribuições são bem-vindas! 
 
## Licensa
 
Este projeto está licensiado sob a [Licensa MIT](LICENSE).
