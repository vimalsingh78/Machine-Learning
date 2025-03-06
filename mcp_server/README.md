# MCP Server

A local implementation of Mission Control Protocol (MCP) server.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Features

- FastAPI-based REST API
- OAuth2 authentication
- Message handling
- SQLite database
- Swagger documentation

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload
```

## Security Note

The default configuration uses simple token-based authentication and an SQLite database.
For production use, please:
1. Change the SECRET_KEY in config.py
2. Use a more robust database
3. Implement proper authentication
4. Add rate limiting
5. Enable HTTPS
