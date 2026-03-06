# Problem Understanding Service – Bruno API Collection

Use com [Bruno](https://www.usebruno.com/):

1. Abra o Bruno e adicione esta pasta como collection (**Open Collection** → selecione a pasta `bruno`).
2. Selecione o environment **local** (barra superior ou menu de ambientes) para usar `base_url: http://localhost:8000`.
3. Suba o serviço: `uv run python main.py` ou via Docker na porta 8000.
4. Execute as requisições na ordem desejada.

## Requisições

| Nome | Método | Descrição |
|------|--------|-----------|
| **Health Check** | `GET /health` | Verifica se o serviço está no ar. Retorna `{"status": "ok"}`. |
| **Evaluate Understanding** | `POST /evaluate-understanding` | Exemplo de resposta correta. Esperado: `{"result": "CORRETO"}`. |
| **Evaluate Understanding (resposta errada)** | `POST /evaluate-understanding` | Resposta que descreve produto em vez de soma. Esperado: `{"result": "ERRADO"}`. |
| **Evaluate Understanding (422 - body inválido)** | `POST /evaluate-understanding` | Body sem `interpretacao_saida`. Esperado: `422 Unprocessable Entity`. |

## Environment

O environment **local** está em `environments/local.bru` com:

- `base_url`: `http://localhost:8000`

As URLs das requisições usam `{{base_url}}`, então ao trocar de ambiente (ex.: homolog/prod) basta alterar o environment.
