# Questão 2 - Organização de Tarefas e Multas
# Algoritmo guloso: ordenar por multa decrescente
# Matrícula: 516833


def organizar_tarefas(tarefas):
    n = len(tarefas)

    # Ordena por multa decrescente (índice 2 da tupla)
    ordenadas = sorted(tarefas, key=lambda t: t[2], reverse=True)

    # agenda[0] não é usada; dias de 1 até n
    agenda = [None] * (n + 1)
    atrasadas = []

    # Para cada tarefa, tenta o último dia livre até o prazo
    for t in ordenadas:
        nome = t[0]
        prazo = t[1]
        multa = t[2]

        dia = min(prazo, n)

        # Procura para trás o último dia livre
        while dia >= 1 and agenda[dia] is not None:
            dia = dia - 1

        if dia >= 1:
            agenda[dia] = t
        else:
            atrasadas.append(t)

    # Preenche dias vazios com tarefas atrasadas
    for dia in range(1, n + 1):
        if agenda[dia] is None:
            tarefa = atrasadas.pop(0)
            agenda[dia] = tarefa

    # Calcula a multa total
    multa_total = 0
    for dia in range(1, n + 1):
        t = agenda[dia]
        prazo = t[1]
        multa = t[2]
        if dia > prazo:
            multa_total = multa_total + multa

    return agenda, multa_total


def imprimir_resultado(tarefas, nome_teste):
    print("=" * 50)
    print(nome_teste)
    print("Tarefas:", tarefas)
    print("-" * 50)

    # Mostra a ordem gulosa
    ordenadas = sorted(tarefas, key=lambda t: t[2], reverse=True)
    print("Ordem por multa (decrescente):")
    for t in ordenadas:
        print(" ", t[0], "- prazo", t[1], "- multa", t[2])

    agenda, multa_total = organizar_tarefas(tarefas)

    print()
    print("Agenda:")
    n = len(tarefas)
    for dia in range(1, n + 1):
        t = agenda[dia]
        nome = t[0]
        prazo = t[1]
        multa = t[2]
        if dia > prazo:
            situacao = "ATRASADA (multa R$ " + str(multa) + ")"
        else:
            situacao = "dentro do prazo"
        print("  Dia", dia, ":", nome, "| prazo", prazo, "|", situacao)

    print()
    print("Multa total mínima: R$", multa_total)
    print()
    return multa_total


def main():
    # Teste 1 - esperado: R$ 20
    t1 = [
        ("A", 1, 20),
        ("B", 2, 50),
        ("C", 1, 40),
        ("D", 3, 10),
    ]
    r1 = imprimir_resultado(t1, "Teste 1 - Uma tarefa atrasada")

    # Teste 2 - esperado: R$ 50
    t2 = [
        ("A", 1, 100),
        ("B", 1, 50),
        ("C", 2, 40),
    ]
    r2 = imprimir_resultado(t2, "Teste 2 - Tarefas com mesmo prazo")

    # Teste 3 - esperado: R$ 0
    t3 = [
        ("A", 1, 20),
        ("B", 2, 30),
        ("C", 3, 40),
    ]
    r3 = imprimir_resultado(t3, "Teste 3 - Todas dentro do prazo")

    # Teste 4 - esperado: R$ 30
    t4 = [
        ("A", 1, 30),
        ("B", 1, 30),
        ("C", 2, 30),
    ]
    r4 = imprimir_resultado(t4, "Teste 4 - Multas iguais")

    print("=" * 50)
    print("Resumo dos resultados:")
    print("  Teste 1: R$", r1, "(esperado 20)")
    print("  Teste 2: R$", r2, "(esperado 50)")
    print("  Teste 3: R$", r3, "(esperado 0)")
    print("  Teste 4: R$", r4, "(esperado 30)")


if __name__ == "__main__":
    main()
