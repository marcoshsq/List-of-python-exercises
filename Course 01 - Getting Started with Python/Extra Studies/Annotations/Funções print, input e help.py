"""Uma introdução informal ao Python＼(^ω^＼).

"""

# A função print() e input()
# Alguns comandos básicos do Python que são importantes:

"""O primeiro comando a aprender é o print(), a função print 
recebe algum objeto e imprime ele na tela ou no console."""

print("Oi, eu sou o computador!")

# E o print tem parâmetros

print("Hello, World!")

print(
    "Hello", "World", sep="**"
)  # esse (sep="") separa as partes da string com o simbolo

print("Hello", end="*-*-*")  # o end coloca o seu conteúdo no final

# Já usando aspas triplas é possível fazer uns print bem loko

print(
    """Oi abigos

    Me llamo Ramon Bolivar           +---+---+---+---+---+---+
                                     | P | y | t | h | o | n |
                                     +---+---+---+---+---+---+
                                     0   1   2   3   4   5   6
                                     -6  -5  -4  -3  -2  -1


	
(づ｡◕‿‿◕｡)づ: (◕‿◕) 		
                                                                (づ｡◕‿‿◕｡)づ: (◕‿◕)
(づ｡◕‿‿◕｡)づ: (◕‿◕)	
(づ｡◕‿‿◕｡)づ: (◕‿◕)
"""
)

# A função input() recebe dados do usuário, e usando concatenção
# e/ou interpolação é possível fazer outros prints u.u

name = input("What's is your name? ")

print(f"Hi {name}, nice to meet you!")
print("Hi {}, nice to meet you!".format(name))
print("Hi", name + ", nice to meet you!")

"""Mais sobre a função print() 

"""

# String é texto, e no python não há diferença de string e char's
# Uma string de apenas 1 character é uma string pequenininha u.u

"Podemos declarar string com aspas duplas"
"Ou com aspas simples"
"Como a maioria dos textos são em inglês e usa-se muito o ', eu vou usar aspas duplas"

# existem operações que podem ser feitas com strings e a função print()
print("Por exemplo, colocar \ngera uma nova linha")
print("Na verdade o contra barra é um character especial")
# E dependendo com quem ele está, ele gera um comando diferente
# \n pula linha
# \a coloca um ponto na frase, tipo para lista

# Para evitar isso coloca-se um r antes das aspas, dizendo para o python que
# essa string é uma raw string u.u
print("O\n babaiaga")
print("O\a babaiaga")
print(r"O\n babaiaga")
print(r"O\a babaiaga")

# Existem outras formas de fazer um print que são muito hacker man!
print(
    "Essa forma aqui, "
    "a frase ainda vai "
    "printada na mesma linha "
    r"caso eu não use \n por exemplo"
)

# Dá para fazer concatenação de strings:

a = "Bola falando: "
b = "Karalho Zé... "
c = "Vai ser pai de novo..."
print(a + b + c)  # Não a diferença entre o mais e a virgula,
print(a, b, c)  # Mas, para concatenação, vou continuar usando o sinal de mais

# Também é possível multiplicar carácteres:

print("Oi " * 10)
print("-=-" * 25)

# String index: Strings podem ser indexadas (subscritos),
# com o primeiro caractere tendo índice 0:

teste = "123456789"
teste[1]

# Os índices também podem ser números negativos, para começar a contar da direita:

teste[-1]

# Além da indexação, o fatiamento também é suportado.
# Enquanto a indexação é usada para obter caracteres individuais,
# o fatiamento permite obter a substring:

teste[1:5]

(
    teste[:3] + teste[3:]
)  # Observe como o início é sempre incluído e o fim sempre excluído.
# Isso garante que s[:i] + s[i:] seja sempre igual a s:

# Strings são imutáveis, não é possível adicionar caracteres depois
# pra isso crie uma nova string u,u

# A função len da o tamanho de uma string:

nome = "Marcos"
len(nome)

###

"""Função help()

"""

# A função help recebe um objeto como parâmetro
# e devolve as funcionalidades do objeto
help(str)  # Help on class str in module builtins
help(tuple)  # Help on class tuple in module builtins

"""None 

É uma constante especial em Python que representa a 
ausência de um valor ou valor nulo.

É um objeto de seu próprio tipo de dados, o NoneType. 
Não podemos criar vários objetos None, mas podemos atribuí-los
a variáveis. Essas variáveis serão iguais entre si.
"""

None == 0  # Retorna False
None == []  # Retorna False
None == False  # Retorna False
x = None
y = None
x == y  # Retorna True


"""(づ｡◕‿‿◕｡)づ

"""
