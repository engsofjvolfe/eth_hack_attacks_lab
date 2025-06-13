# 🧠 TODO.md — eth_hack_attacks_lab

Este arquivo lista tarefas técnicas pendentes, etapas futuras e ideias organizadas por categoria. O projeto simula um ambiente de aprendizado em hacking ético, separando claramente a estrutura atacante e o servidor vulnerável.

---

## 📦 Estrutura do Projeto (Visão Geral)

- `scanners/`: Scripts de varredura e detecção de serviços/endpoints
- `exploits/`: Ataques específicos (ex: SQLi, brute force)
- `utils/`: Funções auxiliares (requisições, logging, parsing)
- `wordlists/`: Dicionários personalizados ou importados
- `README.md`: Introdução e instruções de uso
- `TODO.md`: Planejamento e evolução contínua

---

## 🚧 Etapas Pendentes

### 🧪 Fase atual: Scanner básico (manual, único arquivo)
- [x] Criar `run_scanner.py` funcional com lista interna de paths
- [x] Detectar código de status e tempo de resposta
- [ ] Validar contra servidor Flask ativo

---

### 🔁 Fase seguinte: Modularização do scanner
- [ ] Criar `utils/http_tools.py` com `get_status_code(url)` e parse
- [ ] Mover lógica de varredura para `scanners/scanner_engine.py`
- [ ] Tornar `run_scanner.py` apenas ponto de entrada
- [ ] Criar `wordlists/common_paths.txt` com lista de endpoints a testar
- [ ] Adicionar suporte a argumentos CLI (`--target`, `--wordlist`, `--verbose`)
- [ ] Adicionar coloração de saída para erros e sucessos

---

### 📈 Futuras funcionalidades (etapas opcionais)
- [ ] Suporte a múltiplos threads (varredura mais rápida)
- [ ] Modo verbose/silencioso via argumento
- [ ] Exportar resultados para JSON ou arquivo `.log`
- [ ] Detecção de WAF ou códigos suspeitos
- [ ] Logging com timestamps
- [ ] Detecção de redirecionamento (`3xx`) e headers suspeitos
- [ ] Identificação de endpoints que retornam erros (`500`, `403`, etc)

---

## 📌 Ideias futuras (não prioritárias)
- Adicionar varredura por portas com `socket`
- Criar runner de exploits simples (ex: script de SQLi automatizado)
- Gerar relatório final com dados dos endpoints encontrados

---

## ✍️ Notas

- A modularização será aplicada apenas após o script funcionar corretamente de ponta a ponta.
- A estrutura seguirá o padrão funcional baseado em **separação de responsabilidade** por diretório.
- Todos os scripts devem ser compatíveis com Termux, priorizando uso local sem dependência gráfica.
