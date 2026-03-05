# teste-prognum-consumo-api
Projeto de consumo de API utilizando requisições do site dummyjson


# Consumo de API - DummyJSON

Projeto Python que consome APIs do serviço DummyJSON para demonstrar requisições GET e POST.

## Descrição

Este projeto realiza três consumos de API:

### a) GET - Buscar usuário por ID
- **URL**: `https://dummyjson.com/user/2`
- **Método**: GET
- **Descrição**: Recupera os dados do usuário com ID 2

### b) POST - Autenticação
- **URL**: `https://dummyjson.com/auth/login`
- **Método**: POST
- **Parâmetros**:
  ```json
  {
    "username": "hbingley1",
    "password": "CQutx25i8r"
  }
  ```
- **Descrição**: Realiza login e extrai o campo `firstName`

### c) GET - Buscar usuário com ID 1
- **URL**: `https://dummyjson.com/user/1`
- **Método**: GET
- **Descrição**: Recupera os dados do usuário com ID 1

## Como Executar

### Pré-requisitos
- Python 3.8+
- Biblioteca `requests`

### Instalação
```bash
pip install requests
```

### Execução
```bash
python consumo_api.py
```

## Estrutura do Projeto

```
consumo_api/
├── consumo_api.py    # Script principal
└── README.md         # Este arquivo
```

## Saída Esperada

O script exibe:
1. Resultado completo da requisição GET /user/2
2. Resultado da requisição POST /auth/login com destaque para o campo firstName
3. Resultado completo da requisição GET /user/1

Todas as respostas são formatadas em JSON para melhor legibilidade.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Requests**: Biblioteca para requisições HTTP
- **DummyJSON**: API pública para testes

## Notas

- As credenciais utilizadas são credenciais de teste do DummyJSON
- Não há autenticação real necessária
- Pode ser necessário verificar a conexão com a internet para acessar as APIs

