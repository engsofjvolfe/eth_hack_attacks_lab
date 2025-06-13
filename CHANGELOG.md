# 📘 CHANGELOG — eth_hack_attacks_lab

Este changelog registra a evolução técnica do projeto, com foco em rastreabilidade clara entre TODOs, commits e progresso real. Cada entrada pode ser referenciada no Git, no `TODO.md`, ou nos documentos reflexivos.

---

## 📅 2025-06-12 — Estrutura inicial e scanner básico

🔁 Commit: `feat: estrutura inicial do projeto com scanner funcional`

- Cria estrutura principal do projeto:
  - `scanners/`, `exploits/`, `utils/`, `wordlists/`
- Implementa script funcional de varredura:
  - `scanners/run_scanner.py` faz requests HTTP a paths predefinidos
  - Mostra código de status e tempo de resposta
- Adiciona arquivos vazios para expansão futura:
  - `exploits/sql_injection_test.py`, `utils/http_tools.py`, etc.
- Adiciona `.gitignore` padrão e `requirements.txt` com `requests`
- Adiciona documentação básica:
  - `CHANGELOG.md`, `README.md`, `INTRO.md`, `etapas_detalhadas.md`, `roteiro.md`  
- Rastreia as tarefas do TODO.md:
  - `[x] Criar run_scanner.py funcional`
  - `[x] Detectar código de status e tempo de resposta`

✍️ Observações:
- Esta etapa foi feita diretamente na `main`, pois marca o início do projeto.
- A partir da próxima tarefa, branches atômicas serão usadas para cada evolução técnica.

---

