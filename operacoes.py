from operacoes import reprovado, imprimir_reprovados

# Informações sobre os alunos
alunos = {
    26: {'nome': 'Maria', 'notas': [8, 7 ,5 ,9]},
    101: {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    13: {'nome': 'João', 'notas': [6, 5, 5, 5]},
    37: {'nome': 'Ágatha', 'notas': [8, 6, [7,5], 9]},
    72: {'nome': 'Joaquim', 'notas': [6, [5,5], 5, 7]},
    5: {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
}

# Procurar alunos reprovados
reprovados = []
for matricula, aluno in alunos.itens():
    media = calcular_media(aluno['notas'])
    if reprovado(media):
        reprovados.append(matricula)

# Imprimir resultado
imprimir_reprovados(alunos, reprovados)

def calcular_media(notas):
   '''''Calcular a média aritimética das notas.

    Args: 
        notas: Uma lista contendo as notas dos quatro bimestres.
    
    Returns:
    A média aritmética das notas.
    
    '''''
   return sum(notas) / len(notas)

def reprovado(media):
    '''''Verificar se o aluno foi reprovado.

    Args: 
        media: A média do aluno.
    
    Returns: 
        True se o aluno estiver reprovado (media < 6),
    '''''
    return media < 6

def imprimir_reprovados(alunos, reprovados):
    """Imprimir os dados dos alunos reprovados.
     
       Args:
          alunos: Um dicionário com os dados dos alunos.
          reprovados: Uma lista com as matrículas dos alunos reprovados.
    """
    for matricula in reprovados:
        aluno = alunos[matricula]
        media = calcular_media(aluno['notas'])
        print(f"Aluno reprovado: {aluno['nome']} - Matrícula: {matricula} - Média Final: {media}")