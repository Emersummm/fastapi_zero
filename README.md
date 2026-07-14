# FastAPI Zero

Uma aplicação moderna construída com [FastAPI](https://fastapi.tiangolo.com/) e Python.

## 📋 Sobre o Projeto

Este é um projeto FastAPI que implementa uma API RESTful com autenticação, validação de dados e documentação automática.

## ✨ Funcionalidades

- ⚡ API rápida e moderna com FastAPI
- 📚 Documentação automática (Swagger/OpenAPI)
- 🔐 Autenticação e autorização
- 🗄️ Integração com banco de dados
- ✅ Validação de dados com Pydantic
- 🧪 Testes unitários
- 📦 Gerenciamento de dependências com Poetry

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.9+
- [Poetry](https://python-poetry.org/) (opcional, para gerenciamento de dependências)
- pip (gerenciador de pacotes padrão do Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/fastapi_zero.git
cd fastapi_zero
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou com Poetry:
```bash
poetry install
```

### Executar a Aplicação

```bash
uvicorn fastapi_zero.main:app --reload
```

A API estará disponível em `http://localhost:8000`

## 📖 Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🗂️ Estrutura do Projeto

```
fastapi_zero/
├── fastapi_zero/
│   ├── __init__.py
│   ├── main.py              # Arquivo principal da aplicação
│   ├── models/              # Modelos de dados (Pydantic)
│   ├── routes/              # Rotas/endpoints da API
│   ├── schemas/             # Schemas de requisição/resposta
│   └── database.py          # Configuração do banco de dados
├── tests/
│   ├── __init__.py
│   └── test_*.py            # Testes unitários
├── pyproject.toml           # Configuração do Poetry
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

## 🔧 Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

## 🧪 Testes

Execute os testes com:

```bash
pytest
```

Para ver cobertura de testes:
```bash
pytest --cov=fastapi_zero
```

## 📦 Dependências Principais

- **fastapi** - Framework web
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM
- **pydantic** - Validação de dados
- **python-jose** - Autenticação JWT
- **pytest** - Testes
- **httpx** - Cliente HTTP para testes

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Suporte

Para suporte, abra uma issue no [GitHub Issues](https://github.com/seu-usuario/fastapi_zero/issues).

## 📚 Recursos Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
