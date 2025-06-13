# 📘 Etapas detalhadas — eth_hack_attacks_lab

Este documento registra de forma narrada e técnica o progresso prático do projeto. Cada etapa segue o roteiro educacional definido na introdução, com foco real em aprendizado, rastreabilidade e construção de sistemas com sentido.

---

## 1. 🧰 Preparação do ambiente

### ✅ O que foi feito
- Iniciei o projeto no computador (Ubuntu), apesar de a ideia original envolver rodar os testes ofensivos no celular com root. Decidi começar por aqui para facilitar a documentação, commits e aprendizado organizado.
- Criei repositório local e remoto no GitHub com nome `eth_hack_attacks_lab`.
- Organizei a estrutura inicial de pastas:
  - `scanners/`, `exploits/`, `utils/`, `wordlists/`, `docs/`
- Criei ambiente virtual Python com `venv`
- Instalei a biblioteca `requests` e gerei `requirements.txt`
- Iniciei arquivos vazios para futuras expansões
- Configurei `.gitignore` para ignorar `__pycache__/`, `*.pyc` e `.venv/`
- Criei os arquivos iniciais de rastreio: `TODO.md`, `CHANGELOG.md`, `README.md`

**Observação:** Os conteúdos técnicos das pastas serão explorados nas próximas etapas.

---

### 🧪 Passo a passo realizado

> Tudo foi feito manualmente, com registro intencional. Isso aqui não é só um checklist — é minha história real com esse projeto. Você pode seguir esse passo a passo.

#### 1.1 – Criação do repositório local

```bash
mkdir eth_hack_attacks_lab   # Cria a pasta principal do projeto
cd eth_hack_attacks_lab      # Entra na pasta recém-criada
git init                     # Inicializa um repositório Git vazio
```

#### 1.2 – Criação do repositório remoto

- No GitHub, criei o repositório com o mesmo nome.
- Após criar, configurei o remoto localmente com o seguinte comando:

```bash
git remote add origin https://github.com/engsofjvolfe/eth_hack_attacks_lab.git  # Conecta o repositório local ao remoto no GitHub
```

> 🌀 *Observação:* Inicialmente, o Git local criou a branch `master`, pois essa ainda é a configuração padrão em muitos ambientes. Eu alterei o nome da branch remota no GitHub para `main`, mas fiquei com dúvidas sobre como garantir isso também no repositório local.  
>
> Após pesquisar, aprendi que é possível forçar o Git a sempre usar `main` como padrão com o seguinte comando global:

```bash
git config --global init.defaultBranch main  # Define 'main' como branch padrão para todos os novos repositórios
```

> Isso garante que todo novo repositório iniciado com `git init` já comece na branch `main`.

> Para o repositório atual (que já estava em `master`), também é possível renomear manualmente:

```bash
git branch -m master main       # Renomeia a branch local de 'master' para 'main'
git push -u origin main         # Envia a nova branch para o GitHub e define como upstream
```

> Depois disso, basta garantir nas configurações do GitHub (Settings > Branches) que `main` está como a branch principal, e remover a `master` se não for mais usada.

---

#### 1.3 – Configuração da estrutura de pastas

```bash
mkdir scanners exploits utils wordlists docs   # Cria as pastas principais do projeto
touch README.md .gitignore TODO.md CHANGELOG.md  # Cria os arquivos iniciais de documentação e controle
```

---

#### 1.4 – Criação do ambiente virtual

```bash
python3 -m venv .venv        # Cria um ambiente virtual isolado na pasta .venv
source .venv/bin/activate    # Ativa o ambiente virtual no terminal atual
```

---

#### 1.5 – Instalação da dependência principal

- A biblioteca `requests` permite realizar requisições HTTP em Python com facilidade.
- Para este projeto, ela será usada nos scanners e nos testes de ataques simulados.

```bash
pip install requests                # Instala a biblioteca requests no ambiente virtual
pip freeze > requirements.txt      # Gera o arquivo de dependências com as versões atuais
```

> Assim, qualquer pessoa pode executar:

```bash
pip install -r requirements.txt    # Instala automaticamente todas as dependências listadas
```

> E ter o ambiente pronto para uso.

---

#### 1.6 – Primeiros arquivos criados

```bash
touch scanners/run_scanner.py             # Script principal do scanner (a ser expandido)
touch exploits/sql_injection_test.py      # Placeholder para futuro teste de SQL Injection
touch utils/http_tools.py                 # Funções auxiliares para requisições HTTP
touch wordlists/common_paths.txt          # Lista de caminhos a serem testados pelos scanners
```

---

#### 1.7 – Diferença entre cliente e servidor no laboratório

- O **servidor vulnerável** (repositório complementar [eth_hack_server_lab](https://github.com/engsofjvolfe/eth_hack_server_lab)) roda um app Flask com falhas intencionais. Ele simula um ambiente exposto na rede, como se fosse uma aplicação real.
- O **cliente atacante** (este projeto) executa scripts que interagem com esse servidor, realizando testes e análises para aprendizado ofensivo.
- Ambos fazem parte do mesmo laboratório local, porém com papéis totalmente separados.

---

#### 1.8 – Garantia de comunicação entre cliente e servidor

- O servidor Flask foi iniciado com IP local detectado automaticamente, usando o script Python `run_server.py` (ou manualmente com `python app.py` - projeto no repositório `eth_hack_server_lab`).
- Do lado do cliente (este repositório), testei a comunicação executando diretamente o script `scanners/run_scanner.py`:

```bash
python scanners/run_scanner.py #executa o script que se comunica com o servidor
```

- Ao ser solicitado, digitei diretamente a URL `http://192.168.x.x:5000/login`, uma das rotas já disponíveis no servidor vulnerável.

- O script (`run_scanner.py`, versão básica) realizou uma requisição `GET` para essa rota e obteve uma resposta com `200 OK`, confirmando que a comunicação entre cliente e servidor estava funcional.

- Com isso, a estrutura local está validada e pronta para os testes ofensivos das próximas etapas.


---

### 🎯 Aprendizado/reflexão

- Vi claramente que **entender o fluxo de criação de um projeto do zero** me dá mais segurança para evoluir depois, mesmo que o projeto ainda seja simples.
- Estou praticando não só código, mas também organização, clareza e rastreamento. Esse é meu foco aqui.
- A separação entre **servidor vulnerável** e **cliente atacante** começou a fazer mais sentido conforme fui documentando.
- Essa documentação me dá confiança de que posso parar e retomar sem me perder — e até mostrar esse material futuramente, se quiser.
