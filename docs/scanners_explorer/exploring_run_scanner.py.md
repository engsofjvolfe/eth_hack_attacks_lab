# 🔎 `run_scanner.py` — Verificação básica de comunicação

Este documento explica o funcionamento do script `scanners/run_scanner.py`, criado especificamente para a etapa **1.8** do projeto, cujo objetivo é verificar se o servidor vulnerável está ativo e acessível a partir do cliente atacante.

---

## 🎯 Propósito do script

- Confirmar que o servidor está **ativo** e **acessível** pela rede local.
- Realizar uma requisição HTTP `GET` básica para testar a conectividade.
- Exibir o **status HTTP** retornado (`200`, `404`, `500` etc.).
- Capturar e exibir erros de conexão (ex: IP incorreto, servidor desligado).
- Servir como **primeiro contato prático** entre cliente e servidor no laboratório.

---

## 📄 Código-fonte com explicações (linha a linha)

```python
# Importa a biblioteca requests, usada para enviar requisições HTTP
import requests

# Define a função principal do script
def basic_scan():
    """
    Solicita uma URL do usuário e tenta realizar uma requisição GET.

    - Adiciona 'http://' automaticamente se não estiver presente.
    - Exibe o status HTTP retornado pelo servidor.
    - Captura e exibe erros comuns de conexão.
    """

    # Solicita ao usuário a URL completa do servidor para teste
    url = input("URL completa para teste (ex: http://192.168.0.10:5000): ").strip()

    # Verifica se o usuário esqueceu de informar o protocolo
    # Se não começou com 'http://' nem 'https://', adiciona 'http://' por padrão
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        # Realiza uma requisição GET com tempo limite de 5 segundos
        response = requests.get(url, timeout=5)

        # Exibe o código de status HTTP retornado pelo servidor
        print(f"Status: {response.status_code}")

    except requests.RequestException as e:
        # Em caso de erro na requisição, exibe a mensagem de erro
        print(f"Erro: {e}")

# Executa a função apenas se o script for rodado diretamente
if __name__ == "__main__":
    basic_scan()
```

---

## 🧱 Etapa relacionada

- [1.8 – Garantia de comunicação entre cliente e servidor](/docs/etapas_detalhadas.md#18--garantia-de-comunicação-entre-cliente-e-servidor)

---

## 📁 Local do arquivo no projeto

```
eth_hack/
└── scanners/
    └── run_scanner.py
```

---

## ✅ Resultado esperado

Se o servidor estiver rodando e a URL for válida, o terminal exibirá algo como:

```
Status: 200
```

Se houver erro de rede ou endereço inválido, o terminal mostrará algo como:

```
Erro: HTTPConnectionPool(...) — Connection refused
```

---

## 🧩 Observações finais

- A função desse script é **verificar se o servidor responde a uma requisição GET simples**.
