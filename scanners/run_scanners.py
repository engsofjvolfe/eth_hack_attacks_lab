"""
Script de verificação inicial de comunicação com o servidor.

Realiza uma requisição HTTP `GET` simples para um endereço informado pelo usuário.
Serve para testar se o servidor está ativo e respondendo corretamente.

Este script é usado na Etapa 1.8 apenas como verificação de estrutura cliente-servidor.
"""

import requests

def basic_scan():
    """
    Solicita uma URL do usuário e tenta realizar uma requisição GET.

    - Adiciona o prefixo 'http://' automaticamente se não for informado.
    - Exibe o código de status HTTP retornado pelo servidor.
    - Em caso de erro (ex: conexão recusada), exibe a exceção capturada.

    Obs: Essa etapa **não analisa tempo de resposta, nem testa múltiplos caminhos**.
    """
    url = input("URL completa para teste (ex: http://192.168.0.10:5000): ").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        response = requests.get(url, timeout=5)
        print(f"Status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    basic_scan()