# Montagem de CRUD — versão 1

## O que este projeto faz
Este projeto implementa um CRUD (Create, Read, Update, Delete — **Criar, Ler, Atualizar e Remover**) de **produtos** e seus **valores**.

Além do cadastro e manutenção da lista, a API permite:
- identificar o **produto de maior valor**
- identificar o **produto de menor valor**
- calcular o **valor total** de todos os itens cadastrados

## Como rodar (executar)
No Visual Studio Code, abra o terminal na pasta do projeto e execute:

```bash
python -m uvicorn api_v2:app --reload --host 127.0.0.1 --port 8000