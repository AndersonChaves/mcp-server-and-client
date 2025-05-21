# MCP Server Weather
 
This project is a simple implementation of a server that provides weather information using the MCP (Message Communication Protocol).
 
## Features
 
- Provides weather data for different locations.
- Implements the MCP protocol for communication.
- Lightweight and easy to set up.
 
## Prerequisites
 
- [Python](https://www.python.org/) installed on your system.
- Basic knowledge of MCP protocol.
 
## Usage - Server
 
1. Start the server:
    ```bash
    python server.py
    ```
2. The server will run on `http://localhost:8001` by default.
 
3. Use an MCP client to connect and request weather data.
 
4. Start the client interface:
    ```bash
    streamlit run client.py
    ```
5. Access the interface in your browser at `http://localhost:8501`.
 
## Contributing
 
Contributions are welcome! Please fork the repository and submit a pull request.
 
## License
 
This project is licensed under the [MIT License](LICENSE).