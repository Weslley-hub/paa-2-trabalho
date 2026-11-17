# Questão 1 - Problema da Balsa



def balsa(T, n, L):
    # M[k][A][B] = máximo de carros a partir do carro k
    # com espaço A na pista 1 e B na pista 2
    M = []
    for k in range(n + 2):
        linha_a = []
        for a in range(L + 1):
            linha_b = []
            for b in range(L + 1):
                linha_b.append(0)
            linha_a.append(linha_b)
        M.append(linha_a)

    # Preenche de k = n até 1 (bottom-up)
    for k in range(n, 0, -1):
        for A in range(L + 1):
            for B in range(L + 1):
                melhor = 0

                # Tenta colocar o carro k na pista 1
                if T[k] <= A:
                    valor = 1 + M[k + 1][A - T[k]][B]
                    if valor > melhor:
                        melhor = valor

                # Tenta colocar o carro k na pista 2
                if T[k] <= B:
                    valor = 1 + M[k + 1][A][B - T[k]]
                    if valor > melhor:
                        melhor = valor

                M[k][A][B] = melhor

    return M


def mostrar_pistas(M, T, n, L):
    A = L
    B = L
    k = 1
    pista1 = []
    pista2 = []

    print("Distribuição dos carros:")
    while k <= n and M[k][A][B] > 0:
        # Em empate, prioriza a pista 1
        if T[k] <= A and M[k][A][B] == 1 + M[k + 1][A - T[k]][B]:
            print("  Carro", k, "(comprimento", T[k], ") -> Pista 1")
            A = A - T[k]
            pista1.append(k)
        else:
            print("  Carro", k, "(comprimento", T[k], ") -> Pista 2")
            B = B - T[k]
            pista2.append(k)
        k = k + 1

    # Carros que não embarcaram
    while k <= n:
        print("  Carro", k, "(comprimento", T[k], ") -> não embarcado")
        k = k + 1

    usado1 = L - A
    usado2 = L - B
    print("Pista 1: carros", pista1, "| usado:", usado1, "| restante:", A)
    print("Pista 2: carros", pista2, "| usado:", usado2, "| restante:", B)


def resolver(L, carros, nome_teste):
    n = len(carros)
    # Índice começa em 1; posição 0 não é usada
    T = [0] + carros

    print("=" * 50)
    print(nome_teste)
    print("L =", L, "| carros =", carros)
    print("-" * 50)

    M = balsa(T, n, L)
    maximo = M[1][L][L]
    print("Máximo de carros embarcados:", maximo)
    mostrar_pistas(M, T, n, L)
    print()
    return maximo


def main():
    # Teste 1 - esperado: 4 carros
    r1 = resolver(10, [6, 4, 7, 3, 5], "Teste 1")

    # Teste 2 - esperado: 4 carros
    r2 = resolver(10, [6, 6, 4, 4], "Teste 2")

    # Teste 3 - esperado: 2 carros
    r3 = resolver(10, [8, 8, 3], "Teste 3")

    # Teste 4 - esperado: 0 carros
    r4 = resolver(5, [6, 2, 2], "Teste 4")

    print("=" * 50)
    print("Resumo dos resultados:")
    print("  Teste 1:", r1, "(esperado 4)")
    print("  Teste 2:", r2, "(esperado 4)")
    print("  Teste 3:", r3, "(esperado 2)")
    print("  Teste 4:", r4, "(esperado 0)")


if __name__ == "__main__":
    main()
