# Modal FastAPI Starter Template

A production-ready template for building scalable FastAPI applications using Modal's serverless infrastructure.

## 🚀 Features

- FastAPI integration with Modal's serverless platform
- Built-in authentication middleware
- CORS support
- Modular project structure
- Environment variable management
- Example endpoint implementation

## 📋 Prerequisites

- Python 3.8+
- [Modal](https://modal.com) account and CLI installed
- FastAPI

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/modal-fastapi-starter.git
cd modal-fastapi-starter
```

2. Set up a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install individual packages
pip install modal fastapi[standard]
```

4. Set up Modal:
```bash
modal login
```

5. Create a Modal secret for authentication:
```bash
modal secret create auth-token AUTH_TOKEN=your-secret-token
```

## 🏗️ Project Structure

```
modal-fastapi-starter/
├── src/
│   ├── index.py      # Main application file
│   └── classA.py     # Example class implementation
└── utils/            # Utility functions
```

## 🚀 Usage

1. Serving local endpoint (for testing):
```bash
modal serve -m src.api
```

2. Deploy to Modal:
```bash
modal deploy -m src.api
```

## 🔒 Authentication

The template includes a simple token-based authentication system. To access protected endpoints:

1. Include the token in your requests:
```bash
curl -H "Authorization: Bearer your-secret-token" https://your-modal-url/endpoint
```

## 📝 Example Endpoint

The template includes a protected endpoint at `/endpoint` that demonstrates:
- Bearer authentication
- JSON response

To-do:
- OOP/Class integration

## 🔧 Configuration

- Environment variables are managed through Modal secrets
- CORS is configured to allow all origins (customize as needed)
- Authentication token is managed through Modal secrets

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Modal](https://modal.com/) for the serverless infrastructure
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework 