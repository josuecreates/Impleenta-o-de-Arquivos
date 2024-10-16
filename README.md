# Gerenciador de Memória em Python

## Descrição

Este é um projeto simples em Python que simula a gestão de memória de um sistema. Ele permite adicionar, visualizar e remover dados em um vetor de 32 bytes, representando a memória disponível. O programa acompanha o uso de memória, exibindo o espaço livre e controlando a inserção e exclusão de palavras, com um sistema de verificação de espaço e visualização do estado atual da memória.

## Funcionalidades

- **Adicionar**: Insere uma palavra no vetor de memória, caso haja espaço suficiente.
- **Ler**: Exibe o estado atual do vetor, mostrando as palavras alocadas e os espaços disponíveis.
- **Remover**: Permite remover uma palavra da memória, liberando os blocos de bytes que ela ocupava.
- **Memória Limitada**: O vetor tem capacidade limitada de 32 bytes, simulando a gestão de uma memória física com espaço fixo.

## Estrutura do Código

- O código utiliza um **vetor** para simular a memória, onde cada posição pode armazenar uma letra.
- A função `ler` exibe o estado atual da memória, facilitando a visualização.
- O **dicionário** armazena as palavras e seus respectivos índices no vetor, o que facilita as operações de remoção e leitura.
- O programa se encerra automaticamente quando a memória está cheia, ou quando o usuário escolhe a opção de sair.

## Exemplo de Uso

```bash
[1] Adicionar
[2] Ler
[3] Remover
[4] Para finalizar

Memória livre atual: 28
Faça sua escolha: 1
Digite para inserir: teste
Adicionando...
teste adicionado com sucesso!
