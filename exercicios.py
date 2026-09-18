# ============================================================
# EXERCÍCIO 1 - SÃO MÚLTIPLOS
# ============================================================

a = int(input())
b = int(input())

# Verifica se A é múltiplo de B ou se B é múltiplo de A
if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


# ============================================================
# EXERCÍCIO 2 - ORDENAR TRÊS NÚMEROS
# ============================================================

a = int(input())
b = int(input())
c = int(input())

# Guarda os valores na ordem original
original = [a, b, c]

# Cria uma cópia para ordenar
ordenados = original.copy()

# Ordena do menor para o maior
ordenados.sort()

# Mostra os valores em ordem crescente
for numero in ordenados:
    print(numero)

# Linha em branco
print()

# Mostra os valores na ordem em que foram digitados
for numero in original:
    print(numero)


# ============================================================
# EXERCÍCIO 3 - NÚMEROS ÍMPARES
# ============================================================

x = int(input())

# Percorre todos os números de 1 até X
for numero in range(1, x + 1):

    # Verifica se o número é ímpar
    if numero % 2 != 0:
        print(numero)


# ============================================================
# EXERCÍCIO 4 - QUANTIDADE DE LINHAS
# ============================================================

n = int(input())

# O enunciado informa que N representa
# a quantidade de linhas que devem ser impressas.
#
# ATENÇÃO:
# O exemplo específico de saída deste exercício
# não aparece no conteúdo disponível do PDF.
#
# Portanto, a estrutura do exercício é:
#
# for i in range(n):
#     print(...)


# ============================================================
# EXERCÍCIO 5 - MÁQUINA DE CAFÉ
# ============================================================

a1 = int(input())
a2 = int(input())
a3 = int(input())

# Caso a máquina fique no primeiro andar:
# pessoas do segundo andar percorrem 2 andares no total
# pessoas do terceiro andar percorrem 4 andares no total
tempo1 = a2 * 2 + a3 * 4

# Caso a máquina fique no segundo andar:
# pessoas do primeiro andar percorrem 2 andares no total
# pessoas do terceiro andar percorrem 2 andares no total
tempo2 = a1 * 2 + a3 * 2

# Caso a máquina fique no terceiro andar:
# pessoas do primeiro andar percorrem 4 andares no total
# pessoas do segundo andar percorrem 2 andares no total
tempo3 = a1 * 4 + a2 * 2

# Escolhe o menor tempo
resultado = min(tempo1, tempo2, tempo3)

print(resultado)


# ============================================================
# EXERCÍCIO 6 - CONTADOR DE COMBUSTÍVEIS
# ============================================================

alcool = 0
gasolina = 0
diesel = 0

while True:

    codigo = int(input())

    # Código 4 encerra o programa
    if codigo == 4:
        break

    # Código 1 = Álcool
    elif codigo == 1:
        alcool += 1

    # Código 2 = Gasolina
    elif codigo == 2:
        gasolina += 1

    # Código 3 = Diesel
    elif codigo == 3:
        diesel += 1

    # Qualquer outro código é inválido
    # e deve ser solicitado novamente.

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")


# ============================================================
# EXERCÍCIO 7 - FIZZBUZZ
# ============================================================

n = int(input())

answer = []

# Percorre os números de 1 até N
for i in range(1, n + 1):

    # Deve ser verificado primeiro porque
    # o número precisa ser divisível por 3 e por 5
    if i % 3 == 0 and i % 5 == 0:
        answer.append("FizzBuzz")

    # Divisível somente por 3
    elif i % 3 == 0:
        answer.append("Fizz")

    # Divisível somente por 5
    elif i % 5 == 0:
        answer.append("Buzz")

    # Caso não seja divisível por 3 nem por 5
    else:
        answer.append(str(i))

print(answer)


# ============================================================
# EXERCÍCIO 8 - VAI TER COPA!
# ============================================================

# A entrada possui vários casos de teste
# e termina quando chegar ao EOF.

while True:

    try:
        n = int(input())

    except EOFError:
        break

    # Sem reclamações
    if n == 0:
        print("vai ter copa!")

    # Com reclamações
    else:
        print("vai ter duas!")


# ============================================================
# EXERCÍCIO 9 - FIBONACCI
# ============================================================

n = int(input())

# Primeiros dois valores da sequência
a = 0
b = 1

resultado = []

# Gera os N primeiros números
for i in range(n):

    resultado.append(str(a))

    # Calcula o próximo número
    proximo = a + b

    # Atualiza os valores
    a = b
    b = proximo

# Junta os valores usando espaço,
# evitando espaço depois do último número
print(" ".join(resultado))


# ============================================================
# EXERCÍCIO 10 - ENIGMA
# ============================================================

mensagem = input()
crib = input()

contador = 0

# O crib só pode começar até a posição
# onde ainda caiba completamente dentro da mensagem.
limite = len(mensagem) - len(crib) + 1

for inicio in range(limite):

    posicao_valida = True

    # Compara cada letra do crib com
    # a letra correspondente da mensagem
    for j in range(len(crib)):

        letra_mensagem = mensagem[inicio + j]
        letra_crib = crib[j]

        # Na Enigma uma letra nunca pode
        # ser substituída por ela mesma.
        if letra_mensagem == letra_crib:
            posicao_valida = False
            break

    # Se nenhuma letra coincidiu,
    # essa posição é possível.
    if posicao_valida:
        contador += 1

print(contador)