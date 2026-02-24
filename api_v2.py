from fastapi import FastAPI, HTTPException
from pathlib import Path
from typing import Optional 
import json

app = FastAPI()

def converter_valor(valor: str) -> float:
    valor = valor.strip().replace(",", ".")
    try:
        return float(valor)
    except:
        raise HTTPException(status_code=400, detail="Valor inválido")

produtos = []

ARQUIVO_DB = Path("api_v2_produtos.json")

def carregar_produtos():
    global produtos
    if ARQUIVO_DB.exists():
        produtos = json.loads(ARQUIVO_DB.read_text(encoding="utf-8"))

def salvar_produtos():
    ARQUIVO_DB.write_text(json.dumps(produtos, ensure_ascii=False, indent=2), encoding="utf-8")

carregar_produtos()

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/produtos")
def listar():
    return produtos

@app.post("/produtos")
def cadastrar(produto: str, valor: str):
    produto = produto.strip()

    produto_duplicado = produto.lower()
    for item in produtos:
        if item ["produto"].strip().lower() == produto_duplicado:
            raise HTTPException(status_code=400, detail="Produto já cadastrado")

    if produto == "":
        raise HTTPException(status_code=400, detail="Nenhum produto informado")
    
    valor = converter_valor(valor) 

    if valor <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser maior que zero")
      
    produtos.append({"produto": produto, "valor": valor})
    salvar_produtos()
    return produtos[-1]

@app.delete("/produtos/{indice}")
def remover_produto(indice: int):
    if indice < 0 or indice >= len(produtos):
        raise HTTPException(status_code=404, detail="Indice inexistente")
   
    removido = produtos.pop(indice)
    salvar_produtos()
    return removido  

@app.put("/produtos/{indice}")
def atualizar_produto(indice: int, produto: str, valor: str):
    if indice < 0 or indice >= len(produtos):
        raise HTTPException(status_code=404, detail="Indice inexistente")
    produto = produto.strip()
    if produto == "":
        raise HTTPException(status_code=400, detail="Nenhum produto informado")
    
    valor = converter_valor(valor)

    if valor <= 0:
        raise HTTPException(status_code=400, detail="Número não pode ser 0")
    
    produtos[indice] = {"produto": produto, "valor": valor }
    salvar_produtos()
    return produtos[indice]

@app.patch("/produtos/{indice}")
def atualizar_parcial(indice: int, produto: Optional[str] = None, valor: Optional[str] = None):
    if indice < 0 or indice >= len(produtos):
        raise HTTPException(status_code=404, detail="Indice inexistente")
       
    if produto is not None:
        produto = produto.strip()
        if produto == "":
            raise HTTPException(status_code=400, detail="Nenhum produto informado")
        produtos[indice]["produto"] = produto
   
    if valor is not None:
        valor = converter_valor(valor)
        if valor <= 0:
            raise HTTPException(status_code=400, detail="Valor não pode ser 0")
        produtos[indice]["valor"] = valor
    
    salvar_produtos()
    return produtos[indice]
   
@app.delete("/produtos/")
def limpar_lista():
    produtos[:] = []
    salvar_produtos()
    return {"mensagem": "Lista limpa com sucesso!"}

@app.get("/produtos/total_produtos")
def total():
    total = len(produtos)
    return {"total": total}

@app.get("/produtos/valor_total")
def valor_total():
    soma = 0
    for produto in produtos:
        soma = soma + produto["valor"]
    return {"valor_total": soma}

@app.get("/produtos/maior_valor")
def maior_valor():
    if len(produtos) == 0:
        raise HTTPException(status_code=404, detail="Lista vazia")
    
    item_maior_valor = produtos[0]

    for produto in produtos:
        if produto["valor"] > item_maior_valor["valor"]:
            item_maior_valor = produto

    return item_maior_valor

@app.get("/produtos/menor_valor")
def menor_valor():
    if len(produtos) == 0:
        raise HTTPException(status_code=404, detail="Lista vazia")
    
    item_menor_valor = produtos[0]

    for produto in produtos:
        if produto["valor"] < item_menor_valor["valor"]:
            item_menor_valor = produto

    return item_menor_valor

@app.get("/produtos/busca_produto")
def busca_produto(busca: str):
    
    lista_resultado = []

    busca_produto = busca.strip().lower()

    for produto in produtos:
        if busca_produto in produto["produto"].lower():
            lista_resultado.append(produto)
    
    return lista_resultado

@app.get("/produtos/ordem_valor_crescente")
def ordem_valor_crescente():
    lista_ordenada = sorted(produtos, key=lambda produto: produto["valor"])
    return lista_ordenada

@app.get("/produtos/ordem_valor_decrescente")
def ordem_valor_decrescente():
    lista_ordenada = sorted(produtos, key=lambda produto: produto["valor"], reverse=True)
    return lista_ordenada
    
@app.get("/produtos/{indice}")
def selecionar_indice(indice: int):
    if indice < 0 or indice >= len(produtos):
        raise HTTPException(status_code=404, detail="Indice inexistente")
    
    return produtos[indice]





