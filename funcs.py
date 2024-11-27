import random 



def cadastrarUsuario(nome, email_corp, senha, cargo, lista_funcionarios):
    lista_funcionarios[email_corp] = {'Nome': nome, 'Email': email_corp, 'Senha': senha, 'Cargo': cargo}
    return lista_funcionarios

def login(lista_funcionarios, email_fornecido, senha_fornecida):
    funcionario = lista_funcionarios.get(email_fornecido)
    
    if funcionario is None:
        return "Email não encontrado."
    
    if funcionario['Senha'] == senha_fornecida:
        return funcionario 
    else:
        return "Acesso Negado."
    
def logout():
    print("Você foi desconectado.\n")
    return

def enviarCodigoRecuperacao(email, lista_funcionarios):
    if email not in lista_funcionarios:
        return "Email não encontrado."

    codigo_recuperacao = random.randint(100000, 999999)
    lista_funcionarios[email]['CodigoRecuperacao'] = codigo_recuperacao
    print(f"Código de recuperação enviado para {email}: {codigo_recuperacao}")
    return "Código de recuperação enviado com sucesso."


def redefinirSenha(email, codigo_inserido, nova_senha, lista_funcionarios):
    funcionario = lista_funcionarios.get(email)

    if funcionario is None:
        return "Email não encontrado."
    
    if funcionario.get('CodigoRecuperacao') == codigo_inserido:
        lista_funcionarios[email]['Senha'] = nova_senha
        del lista_funcionarios[email]['CodigoRecuperacao']
        return "Senha redefinida com sucesso."
    else:
        return "Código de recuperação inválido ou expirado."
    

def cadastrarMaquinas(nome_maquina, condicao, ano_fabricacao, numero_serie, lista_maquinas):
    if numero_serie in lista_maquinas:
        print(f"Erro: Já existe uma máquina com o número de série {numero_serie}.")
        return lista_maquinas
    lista_maquinas[numero_serie] = {
        'Nome': nome_maquina,
        'Condicao': condicao,
        'Ano': ano_fabricacao,
        'Numero_de_serie': numero_serie
    }
    return lista_maquinas

def registrarManutencao(numero_serie, data, pecas, custos, observacoes, lista_maquinas):
    if numero_serie not in lista_maquinas:
        print("Erro: Máquina não encontrada.")
        return lista_maquinas
    

    manutencao = {
        'Data': data,
        'Pecas': pecas,  
        'Custos': custos,
        'Observacoes': observacoes
    }
    
    if 'Manutencoes' not in lista_maquinas[numero_serie]:
        lista_maquinas[numero_serie]['Manutencoes'] = []
    
    lista_maquinas[numero_serie]['Manutencoes'].append(manutencao)
    print(f"Manutenção registrada para a máquina {numero_serie}.")
    return lista_maquinas


def editarManutencao(lista_maquinas, numero_serie, manutencao_idx, nova_data=None, novas_pecas=None, novos_custos=None, novas_observacoes=None):
    if numero_serie not in lista_maquinas:
        print("Erro: Máquina não encontrada.")
        return lista_maquinas
    
    manutencoes = lista_maquinas[numero_serie].get('Manutencoes', [])
    if manutencao_idx < 0 or manutencao_idx >= len(manutencoes):
        print("Erro: Manutenção não encontrada.")
        return lista_maquinas
    
    manutencao = manutencoes[manutencao_idx]

    if nova_data:
        manutencao['Data'] = nova_data
    if novas_pecas:
        manutencao['Pecas'] = novas_pecas
    if novos_custos:
        manutencao['Custos'] = novos_custos
    if novas_observacoes:
        manutencao['Observacoes'] = novas_observacoes
    
    print(f"Manutenção {manutencao_idx + 1} da máquina {numero_serie} atualizada.")
    return lista_maquinas



def visualizarManutencoes(numero_serie, lista_maquinas):
    if numero_serie not in lista_maquinas:
        print("Erro: Máquina não encontrada.")
        return
    
    manutencoes = lista_maquinas[numero_serie].get('Manutencoes', [])
    if not manutencoes:
        print("Nenhuma manutenção registrada.")
        return
    
    print(f"Manutenções da máquina {numero_serie}:")
    for i, manutencao in enumerate(manutencoes, start=1):
        print(f"\nManutenção {i}:")
        print(f"Data: {'/'.join(manutencao['Data'])}")
        print(f"Peças: {', '.join(manutencao['Pecas'])}")
        print(f"Custos: R$ {(manutencao['Custos'])}")
        print(f"Observações: {manutencao['Observacoes']}")


def validarManutencao(numero_serie, manutencao_idx, status, lista_maquinas):
    if numero_serie not in lista_maquinas:
        print("Erro: Máquina não encontrada.")
        return lista_maquinas

    manutencoes = lista_maquinas[numero_serie].get('Manutencoes', [])
    if manutencao_idx < 0 or manutencao_idx >= len(manutencoes):
        print("Erro: Manutenção não encontrada.")
        return lista_maquinas


    manutencoes[manutencao_idx]['Validada'] = status
    if status:
        print(f"Manutenção {manutencao_idx + 1} da máquina {numero_serie} validada com sucesso.")
    else:
        print(f"Manutenção {manutencao_idx + 1} da máquina {numero_serie} marcada como não validada.")
    
    return lista_maquinas


def emitirRelatorioPreliminar(numero_serie, lista_maquinas):
    if numero_serie not in lista_maquinas:
        return f"Erro: Máquina com número de série {numero_serie} não encontrada."
    
    maquina = lista_maquinas[numero_serie]
    relatorio = (
        f"Relatório Preliminar\n"
        f"====================\n"
        f"Nome: {maquina['Nome']}\n"
        f"Condição: {maquina['Condicao']}\n"
        f"Ano de Fabricação: {maquina['Ano']}\n"
        f"Número de Série: {maquina['Numero_de_serie']}\n"
    )
    return relatorio

def emitir_relatorio_final(numero_serie, lista_maquinas):
    if numero_serie not in lista_maquinas:
        return f"Erro: Máquina com número de série {numero_serie} não encontrada."
    
    maquina = lista_maquinas[numero_serie]
    relatorio = emitirRelatorioPreliminar(numero_serie, lista_maquinas)
    relatorio += "\nManutenções:\n"

    manutencoes = maquina.get('Manutencoes', [])
    if not manutencoes:
        relatorio += "Nenhuma manutenção registrada.\n"
    else:
        for idx, manutencao in enumerate(manutencoes, start=1):
            validada = manutencao.get('Validada', False)
            relatorio += (
                f"\nManutenção {idx}:\n"
                f"  Data: {'/'.join(manutencao['Data'])}\n"
                f"  Peças: {', '.join(manutencao['Pecas'])}\n"
                f"  Custos: R$ {manutencao['Custos']}\n"
                f"  Observações: {manutencao['Observacoes']}\n"
                f"  Status: {'Validada' if validada else 'Não validada'}\n"
            )
    return relatorio


def cadastrarEvento(id_evento, nome, descricao, data, lista_eventos):
    if id_evento in lista_eventos:
        print(f"Erro: Já existe um evento com o ID {id_evento}.")
        return lista_eventos

    lista_eventos[id_evento] = {
        'Nome': nome,
        'Descrição': descricao,
        'Data': data,
        'Status': 'Aberto'
    }
    print(f"Evento {nome} cadastrado com sucesso!")
    return lista_eventos

def fecharEvento(id_evento, lista_eventos):
    if id_evento not in lista_eventos:
        print(f"Erro: Evento com ID {id_evento} não encontrado.")
        return lista_eventos

    lista_eventos[id_evento]['Status'] = 'Fechado'
    print(f"Evento {lista_eventos[id_evento]['Nome']} foi fechado com sucesso.")
    return lista_eventos

def exibirEventos(lista_eventos):
    if not lista_eventos:
        print("Nenhum evento cadastrado.")
        return

    print("Lista de Eventos:")
    for id_evento, evento in lista_eventos.items():
        print(
            f"\nID: {id_evento}\n"
            f"Nome: {evento['Nome']}\n"
            f"Descrição: {evento['Descrição']}\n"
            f"Data: {evento['Data']}\n"
            f"Status: {evento['Status']}\n"
        )



def cadastrarParticipante(id_evento, nome, telefone, email, lista_eventos):
    if id_evento not in lista_eventos:
        print(f"Erro: Evento com ID {id_evento} não encontrado.")
        return lista_eventos

    evento = lista_eventos[id_evento]
    if evento['Status'] == 'Fechado':
        print(f"Erro: Não é possível adicionar participantes a um evento fechado ({evento['Nome']}).")
        return lista_eventos

    if 'Participantes' not in evento:
        evento['Participantes'] = []

    participante = {'Nome': nome, 'Telefone': telefone, 'Email': email}
    evento['Participantes'].append(participante)
    print(f"Participante {nome} cadastrado no evento {evento['Nome']} com sucesso!")
    return lista_eventos


def exibirParticipantes(id_evento, lista_eventos):
    if id_evento not in lista_eventos:
        print(f"Erro: Evento com ID {id_evento} não encontrado.")
        return

    evento = lista_eventos[id_evento]
    participantes = evento.get('Participantes', [])
    if not participantes:
        print(f"Nenhum participante cadastrado no evento {evento['Nome']}.")
        return

    print(f"Participantes do evento {evento['Nome']}:")
    for idx, participante in enumerate(participantes, start=1):
        print(
            f"\nParticipante {idx}:\n"
            f"  Nome: {participante['Nome']}\n"
            f"  Telefone: {participante['Telefone']}\n"
            f"  Email: {participante['Email']}\n"
        )


def criarQuiz(id_quiz, titulo, lista_quizes):
    if id_quiz in lista_quizes:
        print(f"Erro: Já existe um quiz com o ID {id_quiz}.")
        return lista_quizes

    lista_quizes[id_quiz] = {'Título': titulo, 'Perguntas': []}

    while True:
        pergunta = input("Digite a pergunta: ")
        opcoes = []
        for i in range(4): 
            opcao = input(f"Digite a opção {i + 1}: ")
            opcoes.append(opcao)

        resposta_correta = int(input("Digite o número da resposta correta (1-4): ")) - 1

        lista_quizes[id_quiz]['Perguntas'].append({
            'Pergunta': pergunta,
            'Opções': opcoes,
            'Resposta Correta': resposta_correta
        })

        continuar = input("Deseja adicionar outra pergunta? (s/n): ").lower()
        if continuar != 's':
            break

    print(f"Quiz '{titulo}' criado com sucesso!")
    return lista_quizes

def aplicarQuiz(id_quiz, lista_quizes):
    if id_quiz not in lista_quizes:
        print(f"Erro: Quiz com ID {id_quiz} não encontrado.")
        return

    quiz = lista_quizes[id_quiz]
    print(f"Quiz: {quiz['Título']}")
    acertos = 0
    total_perguntas = len(quiz['Perguntas'])

    for idx, pergunta in enumerate(quiz['Perguntas'], start=1):
        print(f"\nPergunta {idx}: {pergunta['Pergunta']}")
        for i, opcao in enumerate(pergunta['Opções'], start=1):
            print(f"  {i}. {opcao}")

        try:
            resposta = int(input("Digite o número da sua resposta: ")) - 1
            if resposta == pergunta['Resposta Correta']:
                acertos += 1
        except ValueError:
            print("Resposta inválida. Pulando para a próxima pergunta.")

    print(f"\nVocê acertou {acertos} de {total_perguntas} perguntas!")



def formatarFuncionarios(lista_funcionarios):
    if not lista_funcionarios:
        return "Nenhum funcionário cadastrado."

    funcionarios_formatados = []
    for email, dados in lista_funcionarios.items():
        funcionarios_formatados.append(
            f"Nome: {dados['Nome']}, Email: {dados['Email']}, Senha: {dados['Senha']}, Cargo: {dados['Cargo']}"
        )
    return "\n".join(funcionarios_formatados)

def formatarMaquinas(lista_maquinas):
    if not lista_maquinas:
        return "Nenhuma máquina cadastrada."
    
    resultado = "\nLista de Máquinas:\n"
    for numero_serie, dados in lista_maquinas.items():
        resultado += (
            f"- Número de Série: {numero_serie}\n"
            f"  Nome: {dados['Nome']}\n"
            f"  Condição: {dados['Condicao']}\n"
            f"  Ano de Fabricação: {dados['Ano']}\n\n"
        )
    return resultado


def retornarFuncionarios(lista_funcionarios, escolha, email=None):
    match escolha:
        case 1:
            return formatarFuncionarios(lista_funcionarios)
        
        case 2:
            if email is None:
                return 'Você precisa informar o email do funcionário para efetuar a busca.'
            
            funcionario = lista_funcionarios.get(email)
            if funcionario is None:
                return 'Email não encontrado.'
            
            return f"Nome: {funcionario['Nome']}, Email: {funcionario['Email']}, Senha: {funcionario['Senha']}, Cargo: {funcionario['Cargo']} "
        case _:
            return 'Insira uma opção válida.'
        
def exibir_quiz(id_quiz, lista_quizes):
    if id_quiz not in lista_quizes:
        print(f"Erro: Quiz com ID {id_quiz} não encontrado.")
        return

    quiz = lista_quizes[id_quiz]
    print(f"Quiz: {quiz['Título']}")
    for idx, pergunta in enumerate(quiz['Perguntas'], start=1):
        print(f"\nPergunta {idx}: {pergunta['Pergunta']}")
        for i, opcao in enumerate(pergunta['Opções'], start=1):
            print(f"  {i}. {opcao}")
