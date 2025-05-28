# Modal FastAPI Starter Template

A production-ready template for building scalable FastAPI applications using Modal's serverless infrastructure. This template provides a clean, secure, and efficient foundation for deploying ML-powered APIs.

## 🚀 Features

- FastAPI integration with Modal's serverless platform
- Built-in authentication middleware with token-based security
- CORS support
- Modular project structure
- Environment variable management through Modal secrets
- Example class integration
- Protected and public endpoints

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
pip install -r requirements.txt
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
│   ├── app.py        # Main FastAPI application
│   ├── config.py     # Configuration and Modal setup
│   └── model.py      # ML model implementation
├── utils/            # Utility functions
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation
```

## 🚀 Usage

1. Serving local endpoint (for testing):
```bash
modal serve -m src.app
```

2. Deploy to Modal:
```bash
modal deploy -m src.app
```

## 🔒 Authentication

The template includes a token-based authentication system. To access protected endpoints:

1. Include the token in your requests:
```bash
curl -H "Authorization: Bearer your-secret-token" https://your-modal-url/endpoint
```

## 📝 Available Endpoints

- `GET /`: Public endpoint that returns a welcome message and model prediction
- `POST /endpoint`: Protected endpoint that requires authentication

## 🔧 Configuration

- Environment variables are managed through Modal secrets
- CORS is configured to allow all origins (customize as needed)
- Authentication token is managed through Modal secrets
- ML model configuration can be customized in `src/model.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Modal](https://modal.com/) for the serverless infrastructure
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework 