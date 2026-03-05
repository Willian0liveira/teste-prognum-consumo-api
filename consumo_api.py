import requests
import json

# a) Consumir API GET https://dummyjson.com/user/2
print("=" * 60)
print("a) Consumindo GET https://dummyjson.com/user/2")
print("=" * 60)

response_a = requests.get("https://dummyjson.com/user/2")
if response_a.status_code == 200:
    user_data = response_a.json()
    print("Resultado da API GET /user/2:")
    print(json.dumps(user_data, indent=2, ensure_ascii=False))
else:
    print(f"Erro: Status code {response_a.status_code}")

# b) Consumir API POST https://dummyjson.com/auth/login
print("\n" + "=" * 60)
print("b) Consumindo POST https://dummyjson.com/auth/login")
print("=" * 60)

login_data = {
    "username": "hbingley1",
    "password": "CQutx25i8r"
}

response_b = requests.post("https://dummyjson.com/auth/login", json=login_data)

if response_b.status_code == 200:
    login_result = response_b.json()
    print("Resultado da API POST /auth/login:")
    print(json.dumps(login_result, indent=2, ensure_ascii=False))
    print("\n--- Valor do campo firstName ---")
    print(f"firstName: {login_result.get('firstName', 'Campo não encontrado')}")
else:
    print(f"Erro: Status code {response_b.status_code}")
    try:
        print(f"Resposta do servidor: {response_b.json()}")
    except:
        print(f"Resposta do servidor: {response_b.text}")

# c) Considerar a primeira API (user/2) e listar o cliente com ID = 1
print("\n" + "=" * 60)
print("c) Listando cliente com ID = 1 da primeira API")
print("=" * 60)

# Nota: A primeira API retorna um usuário específico, não uma lista
# Então buscaremos o usuário com ID = 1 diretamente
response_c = requests.get("https://dummyjson.com/user/1")
if response_c.status_code == 200:
    user_id_1 = response_c.json()
    print("Dados do cliente com ID = 1:")
    print(json.dumps(user_id_1, indent=2, ensure_ascii=False))
else:
    print(f"Erro: Status code {response_c.status_code}")
