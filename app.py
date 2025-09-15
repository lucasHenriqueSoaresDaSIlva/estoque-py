estoque_atual = {
 "canetas": 150,
 "cadernos": 95,
 "borrachas": 60,
 "lápis": 100,

 "marcadores": 40,
 "colas": 55,
 "papel_sulfite": 200,
 "post-it": 40,
}
movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 50),
    ("lapis", "saída", 40),
    ("marcadores", "entrada", 20),
    ("colas", "saída", 10),
    ("papel sulfite", "saída", 100),
    ("post-it", "entrada", 50),
    ("tesouras", "entrada", 15),         # Produto novo
    ("canetas", "entrada", 30),
    ("cadernos", "saída", 60),
    ("marcadores", "saída", 15),
    ("lapis", "entrada", 20),
    ("apontadores", "entrada", 30),      # Produto novo
    ("post-it", "saída", 60)
]
 
for produto ,tipo , quantidade in movimentacoes_dia:
    if tipo == "entrada":
        if produto in estoque_atual:
            estoque_atual[produto] += quantidade
        else:
            estoque_atual[produto] = quantidade
    elif tipo == "saída":
        if produto in estoque_atual:
            estoque_atual[produto] -= quantidade
        else:
            estoque_atual[produto] = -quantidade
 
produtos_reposicao = [produto for produto,qtd in estoque_atual.items() if qtd <= 50]

print("=== RELATÓRIO DE ESTOQUE ATUALIZADO ===")
for produto, qtd in estoque_atual.items():
    print(f"{produto.title():<15}: {qtd} unidades")

print("\n=== PRODUTOS QUE PRECISAM DE REPOSIÇÃO ===")
if produtos_reposicao:
    for produto in produtos_reposicao:
        print(f"- {produto.title()} (Estoque: {estoque_atual[produto]})")
else:
    print("Nenhum produto precisa de reposição no momento.")

    
    
    
    
    
    
    
    
    
    
    
                                                                                   