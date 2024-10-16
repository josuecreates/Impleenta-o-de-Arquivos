import time  # Biblioteca para adicionar atrasos na execução do código.

# Função responsável por exibir o estado atual do vetor (memória).
def ler():
    print('\nLendo...\n')
    time.sleep(1.5)  # Pausa de 1,5 segundos para simular leitura.
    print(vetor)  # Exibe o conteúdo do vetor.
    print('\n', '=-' * 16)  # Linha de separação para organização visual.

# Inicialização das variáveis.
vetor = [None] * 32  # Cria um vetor de 32 posições, simulando um espaço de memória.
memoria_livre = 32  # Representa a quantidade de bytes livres no vetor (memória).
dicionario = {}  # Dicionário para armazenar palavras e os índices onde elas estão no vetor.

# Exibe o vetor inicial, que está vazio.
print('\nVetor inicial: \n')
print(vetor)
print('\n', '=-' * 16)

# Loop principal do programa.
while True:

    print('[1] Adicionar')  # Opção para adicionar uma palavra.
    print('[2] Ler')  # Opção para ler (visualizar) o estado atual do vetor.
    print('[3] Remover')  # Opção para remover uma palavra.
    print('[4] Para finalizar\n')  # Opção para encerrar o programa.
    print(f'Memória livre atual: {memoria_livre} bytes')  # Exibe a memória disponível.
    escolha = input('\nFaça sua escolha: ')  # Pede ao usuário que escolha uma opção.

    # Adicionar palavra ao vetor.
    if escolha == '1':
        inserir = input("Digite a palavra para inserir: ")  # Entrada da palavra.
        # Verifica se há espaço suficiente no vetor para inserir a palavra.
        if memoria_livre >= len(inserir):
            print('\nAdicionando...')
            time.sleep(1.5)  # Pausa de 1,5 segundos para simular a adição.

            # Verifica os índices livres no vetor (espaços onde está None).
            indices_livres = [i for i, x in enumerate(vetor) if x is None]
            # Se houver espaço suficiente, insere a palavra no vetor.
            if len(indices_livres) >= len(inserir):
                # Adiciona a palavra no vetor e registra os índices usados no dicionário.
                dicionario[inserir] = []
                for i in range(len(inserir)):
                    vetor[indices_livres[i]] = inserir[i]  # Atribui cada letra da palavra a uma posição no vetor.
                    dicionario[inserir].append(indices_livres[i])  # Armazena o índice correspondente no dicionário.

                # Atualiza a quantidade de memória livre.
                memoria_livre -= len(inserir)
                print(f"{inserir} adicionado com sucesso!")

            else:
                print('Memória insuficiente!')  # Se não houver espaço suficiente, exibe mensagem de erro.

        else:
            # Mensagem de erro se a palavra for maior do que o espaço disponível na memória.
            print('\nMemória insuficiente!')
            print(f'Você tem {memoria_livre} bytes de memória livre, mas {inserir} precisa de {len(inserir)} bytes.')

        ler()  # Chama a função de leitura para mostrar o estado do vetor após a adição.

    # Ler o estado atual do vetor.
    elif escolha == '2':
        ler()  # Exibe o vetor no momento atual.

    # Remover palavra do vetor.
    elif escolha == '3':
        if dicionario:  # Verifica se há alguma palavra no dicionário.
            print('\nEscolha a palavra para remover da memória: \n')
            for chave in dicionario.keys():
                print(f'[{chave}]')  # Exibe as palavras disponíveis para remoção.
            remover = input("\nDigite a palavra para remover: ")  # Pede a palavra a ser removida.

            if remover in dicionario:
                # Remove cada letra da palavra do vetor, liberando os espaços.
                for indice in dicionario[remover]:
                    vetor[indice] = None  # Define os espaços da palavra como `None` (libera memória).
                memoria_livre += len(remover)  # Atualiza a quantidade de memória livre.
                del dicionario[remover]  # Remove a palavra do dicionário.
                print(f'\n{remover} removido com sucesso!')
            else:
                print('Palavra não encontrada!')  # Se a palavra não existir no dicionário, exibe erro.

        else:
            print('Nenhuma palavra para remover.')  # Se o dicionário estiver vazio, exibe mensagem.

        ler()  # Exibe o vetor após a remoção.

    # Finalizar o programa.
    elif escolha == '4':
        print('Finalizando...')
        time.sleep(2)  # Pausa para simular o encerramento.
        print('\nPrograma finalizado!')
        break  # Sai do loop, encerrando o programa.

    # Opção inválida (qualquer entrada diferente de 1, 2, 3 ou 4).
    else:
        print('\nOpção inválida, tente novamente!')
        print('\n', '=-' * 16)

    # Verifica se a memória está completamente preenchida.
    if None not in vetor:
        # Se o vetor não tiver mais `None` (todos os espaços preenchidos), o programa encerra.
        print("\nMemória cheia! Encerrando...")
        time.sleep(2)
        print('\nPrograma finalizado!')
        break
