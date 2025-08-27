
# ------------------------------
# Configurações iniciais
# ------------------------------


# Categorias fixas - só essas serão aceitas
categoria_validas = ("comida","bebida","limpeza")

# Set de nomes -> garante que não exista produto duplicado
catalago_nomes = {"arroz","suco_uva","desinfetante"}

# Lista principal de produtos (cada produto é um dicionário)
lista_produtos = [{"nome":"arroz","preco":7.00,"categoria":"comida"},
                  {"nome":"suco_uva","preco":10.00,"categoria":"bebida"},
                  {"nome":"desinfetante","preco":24.00,"categoria":"limpeza"},
                  {"nome":"arroz","preco":7.00,"categoria":"comida"}]

# ------------------------------
# Funções
# ------------------------------
def  cadastra_nomes():

#  Pede o nome do produto e valida duplicados.
#  Retorna um novo nome válido e adiciona ao set de nomes.

    while True:

        nome = input('Digite o nome do produto: ')
        
        if nome in catalago_nomes:
            print('Produto ja cadastrado')
            continue
        else:
            return nome


def cadastra_precos():

# Solicita e valida o preço do produto.

# Pede entrada numérica do usuário
# Converte string para float com tratamento de erro


    while True:
        try:

            preco = float(input('Ditige o valor do produto: '))
            return preco
        except ValueError:
            print('Digite o preço em forma de número real (ex: 10.00)')



def cadastra_categoria():

# Solicita e valida a categoria do produto.

# Pede entrada do usuário para categoria
# Verifica se categoria está na tupla de categorias válidas

    while True:

        categoria = input('Digite a categoria: ')


        # Validação usando tupla (estrutura imutável)
        if categoria in categoria_validas:
            return categoria
        else:
            print('categoria invalida')
            continue


def produto_cadastrado():

# Função principal que orquestra o cadastro completo de um produto.
# Chama funções de validação em sequência
# Monta dicionário completo do produto
# Adiciona produto à lista principal
# Fornece feedback de sucesso
#

    nome = cadastra_nomes()

    preco = cadastra_precos()

    categoria = cadastra_categoria()

    produto = {"nome":nome,"preco":preco,"categoria":categoria}

    lista_produtos.append(produto)

    print("✅ Produto cadastrado com sucesso!")
    return produto
    
while True:
    produto_cadastrado()
    continuar = input("Deseja cadastrar outro produto? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("\n📦 Lista de produtos cadastrados:")
for p in lista_produtos:
    print(p)

