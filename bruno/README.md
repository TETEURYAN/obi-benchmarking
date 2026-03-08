# Problem Understanding Service – Bruno API Collection

Use com [Bruno](https://www.usebruno.com/):

1. Abra o Bruno e adicione esta pasta como collection (**Open Collection** → selecione a pasta `bruno`).
2. Selecione o environment **local** (barra superior ou menu de ambientes) para usar `base_url: http://localhost:8000`.
3. Suba o serviço: `uv run python main.py` ou via Docker na porta 8000.
4. Execute as requisições na ordem desejada.

## Requisições

| Nome | Método | Rota | Descrição |
|------|--------|------|-----------|
| **Health Check** | GET | `/health` | Verifica se o serviço está no ar. Retorna `{"status": "ok"}`. |
| **Evaluate Understanding** | POST | `/evaluate-understanding` | (Legado) Exemplo de resposta correta. Esperado: `{"result": "CORRETO"}`. |
| **Evaluate Understanding (resposta errada)** | POST | `/evaluate-understanding` | (Legado) Resposta que descreve produto em vez de soma. Esperado: `{"result": "ERRADO"}`. |
| **Evaluate Understanding (422 - body inválido)** | POST | `/evaluate-understanding` | (Legado) Body sem `interpretacao_saida`. Esperado: 422 Unprocessable Entity. |
| **Etapa1 - Compreensao** | POST | `/etapa1/compreensao` | Etapa 1 Pólya: questão + respostas às 4 perguntas. Retorna `questao` (resumo) + `perguntas` (status e feedback por pergunta). |
| **Judge - Submit** | POST | `/judge/submit` | Envia código ao Judge externo. Body: `code`, `language`, `problem_id`, `reveal_inputs`. Retorna `passed`, `feedback`, `failed_cases`. |

## Environment

O environment **local** está em `environments/local.bru` com:

- `base_url`: `http://localhost:8000`

As URLs das requisições usam `{{base_url}}`. Para outro ambiente (ex.: homolog/prod), crie um novo environment com o `base_url` desejado.

## Observação

O endpoint **Judge - Submit** depende de um Judge externo em `JUDGE_BASE_URL`. Se o Judge não estiver rodando, a requisição pode retornar 503. Para testes locais sem Judge, use os demais endpoints.
