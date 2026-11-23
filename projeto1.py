alunos = []

def adicionar_aluno():
    nome = input('digite o nome do aluno: ')
    idade = int(input('digite a idade do aluno: '))
    while True:
        nota = float(input('digite a nota do aluno: '))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('nota invalida. Tente novamente por gentileza ^^')
    dados = {
        'nome':nome,
        'idade':idade,
        'nota':nota
    }
    alunos.append(dados)


def listar_alunos():
    if len(alunos) == 0:
        print('sem alunos')
        return
    for aluno in alunos:
        print(f'nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n{'='*30}')


def procurar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('sem alunos no momento.')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            print(f'nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}')
            break
    else:
        print('esse aluno esta fora do sistema.')


def deletar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('sem alunos no momento.')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            alunos.remove(aluno)
            print(f'{nome_do_aluno} deletado com sucesso!')
            break
    else:
        print('esse aluno esta fora do sistema.')

def media_de_notas():
    if len(alunos) == 0:
        print('sem alunos cadastrados.')
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f'a media das notas dos alunos é {media:.2f}')

while True:
    opcao = int(input('o que deseja fazer?\n1. adicionar aluno\n2. listar todos os alunos\n3.buscar aluno pelo nome\n4. remover aluno\n5.mostrar media geral\n6. sair\n'))
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input('qual aluno voce deseja buscar?: ')
            procurar_aluno(nome_aluno)
        case 4:
            nome_aluno = input('qual aluno deseja remover?')
            deletar_aluno(nome_aluno)
        case 5:
            media_de_notas()
        case 6:
            break