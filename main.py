import funcs
import os

lista_funcionarios = {
    'tony.sousa@gmail.com': {'Nome': 'Tony', 'Email': 'tony.sousa@gmail.com', 'Senha': '123', 'Cargo': 'ADM'},
    'Funcionario': {'Nome': 'Funcionario', 'Email': 'funcionario.teste@gmail.com', 'Senha': '123', 'Cargo': 'Funcionario'}
}

lista_maquinas = {
     '115': { 'Nome': 'Maquina1', 'Condicao': 'Nova', 'Ano': '2023', 'Numero_de_serie': '115', 'Manutencoes': [ { 'Data': ['01', '11', '2024'], 'Pecas': ['Filtro de óleo', 'Correia'], 'Custos': 150.75, 'Observacoes': 'Troca de filtro e correia.' } ] }  
}

lista_eventos = {
    '001': {
        'Nome': 'Treinamento de Manutenção',
        'Descrição': 'Treinamento sobre novas tecnicas de manutenção',
        'Data': '2024-12-10',
        'Status': 'Aberto',
        'Participantes': [
            {'Nome': 'Tonho Lopes', 'Telefone': '99999999999', 'Email': 'tonho@gmail.com'}
        ]
    }
}


lista_quizes = {
    '001': {
        'Título': 'Quiz Teste',
        'Perguntas': [
            {
                'Pergunta': 'Qual é a principal função de um trator agrícola?',
                'Opções': ['Plantar sementes', 'Colher grãos', 'Preparar o solo', 'Irrigar as plantas'],
                'Resposta Correta': 2 
            }
        ]
    }
}


while True:
    print('Bem-vindo ao AgroManager.\n1 - Fazer Login\n0 - Sair')
    try:
        escolha = int(input())
    except ValueError:
        print('Digite um número válido.')
        continue

    match escolha:
        case 1:  
            email_fornecido = input('Digite seu email corporativo (professor, seu login é jadson.jose@gmail.com, senha: 123): ')
            senha_fornecida = input('Digite sua senha: ')

            if not email_fornecido or not senha_fornecida:
                print("\nPor favor, preencha tanto o email quanto a senha.")
                continue

            funcionario = funcs.login(lista_funcionarios, email_fornecido, senha_fornecida)

            if funcionario == "Acesso Negado.":
                print(funcionario)

            elif funcionario == "Email não encontrado.":
                print(funcionario)

            else:
                print(f"Bem-vindo, {funcionario['Nome']}!")

                while True:
                    if funcionario['Cargo'] == 'ADM':
                        print('\nMenu Administrador:')
                        print('1 - Cadastrar Funcionários\n2 - Logout\n3 - Mostrar Funcionários\n4 - Recuperar Senha\n5 - Cadastrar Máquinas\n6 - Exibir Máquinas\n7 - Cadastrar Manutenções\n8 - Visualizar Manutenções\n9 - Validar Manutenção \n10 - Emitir relatorio preliminar\n11 - Emitir relatorio final\n12 - Menu de eventos\n 13 - Cadastrar participantes\n14 - Exibir participantes\n 15 - Menu de quizzes')
                    else:
                        print('\nMenu Funcionário:')
                        print('1 - Exibir Informações do Funcionário\n2 - Logout\n3 - Exibir Máquinas\n4 - Recuperar Senha\n5 - Cadastrar Máquinas\n6 - Exivir Máquinas\n7 - Cadastrar Manutenções\n8 - Visualizar Manutenções\n9 - Menu de Eventos\n10 - Cadastrar participantes')

                    try:
                        escolha_acao = int(input("Escolha uma opção: "))
                    except ValueError:
                        print('Digite um número válido.')
                        continue
                    
                    # Comportamento para ADM
                    if funcionario['Cargo'] == 'ADM':
                        match escolha_acao:
                            case 1: 
                                funcionario_info_nome = input('Nome: ')
                                funcionario_info_email = input('Email: ')
                                funcionario_info_senha = input('Senha: ')
                                funcionario_info_cargo = input('Cargo (ADM ou Funcionário): ')

                                lista_funcionarios = funcs.cadastrarUsuario(
                                    funcionario_info_nome,
                                    funcionario_info_email,
                                    funcionario_info_senha,
                                    funcionario_info_cargo,
                                    lista_funcionarios
                                )
                                print("Funcionário cadastrado com sucesso!")

                            case 2:  
                                print("Realizando logout...")
                                break

                            case 3: 
                                print('Digite 1 para listar todos os funcionários ou 2 para buscar um funcionário específico:')
                                try:
                                    escolha_retornar = int(input())
                                    if escolha_retornar == 1:
                                        print("\nLista de Funcionários:")
                                        print(funcs.formatarFuncionarios(lista_funcionarios))
                                    elif escolha_retornar == 2:
                                        funcionario_email = input("Digite o email do funcionário: ")
                                        print(funcs.retornarFuncionarios(lista_funcionarios, 2, funcionario_email))
                                    else:
                                        print("Opção inválida. Tente novamente.")
                                except ValueError:
                                    print("Digite apenas números. Tente novamente.")

                            case 4:  
                                email = input("Digite seu email corporativo: ")
                                print(funcs.enviarCodigoRecuperacao(email, lista_funcionarios))
                                try:
                                    codigo = int(input("Digite o código de recuperação recebido: "))
                                    nova_senha = input("Digite sua nova senha: ")
                                    print(funcs.redefinirSenha(email, codigo, nova_senha, lista_funcionarios))
                                    print("Senha redefinida com sucesso! Retornando ao menu principal...")
                                    break
                                except ValueError:
                                    print("Código inválido. Tente novamente.")

                            case 5: 
                                nome_da_maquina = input('Nome da máquina: ')
                                condicao_maquina = input('Condição: ')
                                ano_fabricacao_maquina = input('Ano de fabricação: ')
                                numero_serie = input('Número de série: ')
                                manutencao = input('Manutenção agendada ou em percusso?')

                                lista_maquinas = funcs.cadastrarMaquinas(
                                    nome_da_maquina,
                                    condicao_maquina,
                                    ano_fabricacao_maquina,
                                    numero_serie,
                                    lista_maquinas
                                )
                                print("Máquina cadastrada com sucesso!")
                                print(lista_maquinas)

                            case 6:
                                print("\nMáquinas Cadastradas:")
                                print(funcs.formatarMaquinas(lista_maquinas))
                            
                            case 7:
                                numero_serie = input("Número de série da máquina: ")
                                data = input("Data da manutenção (DD/MM/AAAA): ")
                                pecas = input("Peças utilizadas (separadas por vírgula): ".split(","))
                                custos = float(input("Custo total: R$ "))
                                observacoes = input("Observações: ")
                                lista_maquinas = funcs.registrarManutenção(numero_serie, data, pecas, custos, observacoes, lista_maquinas)

                            case 8:
                                numero_serie = input("Digite o número de série da máquina: ")
                                funcs.visualizarManutencoes(numero_serie, lista_maquinas)

                            case 9:
                                numero_serie = input("Digite o número de série da máquina: ")
                                funcs.visualizarManutencoes(numero_serie, lista_maquinas) 

                                try:
                                    manutencao_idx = int(input("Digite o número da manutenção que deseja validar (1 para a primeira, 2 para a segunda, etc.): ")) - 1
                                    status = input("Marcar como validada? (s/n): ").lower() == 's'

                                    lista_maquinas = funcs.validarManutencao(numero_serie, manutencao_idx, status, lista_maquinas)
                                except ValueError:
                                    print("Entrada inválida. Tente novamente.")

                            case 10:
                                numero_serie = input("Digite o número de série da máquina: ")
                                relatorio = funcs.emitirRelatorioPreliminar(numero_serie, lista_maquinas)
                                print("\n" + relatorio)
                            
                            case 11:
                                numero_serie = input("Digite o número de série da máquina: ")
                                relatorio = funcs.emitir_relatorio_final(numero_serie, lista_maquinas)
                                print("\n" + relatorio)
                            
                            case 12:

                                print("\nMenu de Eventos:")
                                print("1 - Cadastrar Evento")
                                print("2 - Fechar Evento")
                                print("3 - Exibir Eventos")

                                try:
                                    escolha_evento = int(input("Escolha uma opção: "))
                                except ValueError:
                                    print("Digite um número válido.")
                                    continue

                                if escolha_evento == 1:  
                                    id_evento = input("ID do Evento: ")
                                    nome = input("Nome do Evento: ")
                                    descricao = input("Descrição do Evento: ")
                                    data = input("Data do Evento (YYYY-MM-DD): ")

                                    lista_eventos = funcs.cadastrarEvento(id_evento, nome, descricao, data, lista_eventos)

                                elif escolha_evento == 2:  
                                    id_evento = input("ID do Evento que deseja fechar: ")
                                    lista_eventos = funcs.fecharEvento(id_evento, lista_eventos)

                                elif escolha_evento == 3:  
                                    funcs.exibirEventos(lista_eventos)

                                else:
                                    print("Opção inválida. Tente novamente.")

                            case 13:

                                id_evento = input("Digite o ID do evento: ")
                                nome = input("Nome do Participante: ")
                                telefone = input("Telefone do Participante: ")
                                email = input("Email do Participante: ")

                                lista_eventos = funcs.cadastrarParticipante(id_evento, nome, telefone, email, lista_eventos)

                            case 14: 
                                id_evento = input("Digite o ID do evento: ")
                                funcs.exibirParticipantes(id_evento, lista_eventos)

                            case 15:
                                print("\nMenu de Quizes:")
                                print("1 - Criar Quiz")
                                print("2 - Exibir Quiz")
                                print("3 - Aplicar Quiz")

                                try:
                                    escolha_quiz = int(input("Escolha uma opção: "))
                                except ValueError:
                                    print("Digite um número válido.")
                                    continue

                                if escolha_quiz == 1: 
                                    id_quiz = input("ID do Quiz: ")
                                    titulo = input("Título do Quiz: ")
                                    lista_quizes = funcs.criarQuiz(id_quiz, titulo, lista_quizes)

                                elif escolha_quiz == 2: 
                                    id_quiz = input("ID do Quiz que deseja visualizar: ")
                                    funcs.exibir_quiz(id_quiz, lista_quizes)

                                elif escolha_quiz == 3: 
                                    id_quiz = input("ID do Quiz que deseja aplicar: ")
                                    funcs.aplicarQuiz(id_quiz, lista_quizes)

                                else:
                                    print("Opção inválida. Tente novamente.")

                            case _:
                                print("Opção inválida. Tente novamente.")

                    # Comportamento para Funcionário
                    else:
                        match escolha_acao:
                            case 1:  
                                print(f"\nInformações do Funcionário:\nNome: {funcionario['Nome']}\nEmail: {funcionario['Email']}\nCargo: {funcionario['Cargo']}")

                            case 2: 
                                print("Realizando logout...")
                                break

                            case 3:  
                                print("\nMáquinas Cadastradas:")
                                print(funcs.formatarMaquinas(lista_maquinas))

                            case 4: 
                                email = input("Digite seu email corporativo: ")
                                print(funcs.enviarCodigoRecuperacao(email, lista_funcionarios))
                                try:
                                    codigo = int(input("Digite o código de recuperação recebido: "))
                                    nova_senha = input("Digite sua nova senha: ")
                                    print(funcs.redefinirSenha(email, codigo, nova_senha, lista_funcionarios))
                                    print("Senha redefinida com sucesso! Retornando ao menu principal...")
                                    break
                                except ValueError:
                                    print("Código inválido. Tente novamente.")

                            case 5: 
                                nome_da_maquina = input('Nome da máquina: ')
                                condicao_maquina = input('Condição: ')
                                ano_fabricacao_maquina = input('Ano de fabricação: ')
                                numero_serie = input('Número de série: ')


                                lista_maquinas = funcs.cadastrarMaquinas(
                                    nome_da_maquina,
                                    condicao_maquina,
                                    ano_fabricacao_maquina,
                                    numero_serie,
                                    lista_maquinas
                                )
                                print("Máquina cadastrada com sucesso!")
                            case 6:
                                print("\nMáquinas Cadastradas:")
                                print(funcs.formatarMaquinas(lista_maquinas))

                            case 7:
                                numero_serie = input("Número de série da máquina: ")
                                data = input("Data da manutenção, com espaços EX: 07 10 2024): ").split()
                                pecas = input("Peças utilizadas (separadas por vírgula): ").split(',')
                                custos = float(input("Custo total: R$ "))
                                observacoes = input("Observações: ")
                                lista_maquinas = funcs.registrarManutencao(numero_serie, data, pecas, custos, observacoes, lista_maquinas)

                            case 8:
                                numero_serie = input("Número de série da máquina: ")
                                funcs.visualizarManutencoes(numero_serie, lista_maquinas)

                            case 9:
                                print("\nMenu de Eventos:")
                                print("1 - Cadastrar Evento")
                                print("2 - Fechar Evento")
                                print("3 - Exibir Eventos")

                                try:
                                    escolha_evento = int(input("Escolha uma opção: "))
                                except ValueError:
                                    print("Digite um número válido.")
                                    continue

                                if escolha_evento == 1:  
                                    id_evento = input("ID do Evento: ")
                                    nome = input("Nome do Evento: ")
                                    descricao = input("Descrição do Evento: ")
                                    data = input("Data do Evento (YYYY-MM-DD): ")

                                    lista_eventos = funcs.cadastrar_evento(id_evento, nome, descricao, data, lista_eventos)

                                elif escolha_evento == 2:  
                                    id_evento = input("ID do Evento que deseja fechar: ")
                                    lista_eventos = funcs.fecharEvento(id_evento, lista_eventos)

                                elif escolha_evento == 3:  
                                    funcs.exibirEventos(lista_eventos)

                                else:
                                    print("Opção inválida. Tente novamente.")

                            case 10:
                                id_evento = input("Digite o ID do evento: ")
                                nome = input("Nome do Participante: ")
                                telefone = input("Telefone do Participante: ")
                                email = input("Email do Participante: ")

                                lista_eventos = funcs.cadastrarParticipante(id_evento, nome, telefone, email, lista_eventos)

                            case _:  
                                print("Opção inválida. Tente novamente.")

        case 0: 
            print("Saindo do sistema...")
            break

        case _: 
            print('Digite 0 ou 1 para uma opção válida.')
