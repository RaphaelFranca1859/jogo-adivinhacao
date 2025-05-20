import random
from datetime import datetime

def escolher_dificuldade():
    print("\nEscolha a dificuldade:")
    print("1 - Fácil (15 tentativas)")
    print("2 - Médio (10 tentativas)")
    print("3 - Difícil (5 tentativas)")

    while True:
        escolha = input("Digite 1, 2 ou 3: ")
        if escolha == '1':
            return 15, "Fácil"
        elif escolha == '2':
            return 10, "Médio"
        elif escolha == '3':
            return 5, "Difícil"
        else:
            print("Opção inválida.")

def salvar_pontuacao(nome, dificuldade, tentativas, venceu):
    with open("pontuacoes.txt", "a") as arquivo:
        resultado = "Venceu" if venceu else "Perdeu"
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"{data} - Jogador: {nome} | Dificuldade: {dificuldade} | Tentativas: {tentativas} | Resultado: {resultado}\n")

def jogo_adivinhacao():
    print("🎲 Bem-vindo ao Jogo de Adivinhação!")
    nome = input("Digite seu nome: ")

    max_tentativas, dificuldade = escolher_dificuldade()
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print(f"\nOk, {nome}, adivinhe o número entre 1 e 100. Você tem {max_tentativas} tentativas!")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("🔻 Muito baixo!")
            elif palpite > numero_secreto:
                print("🔺 Muito alto!")
            else:
                print(f"🎉 Parabéns, {nome}! Você acertou em {tentativas} tentativas.")
                salvar_pontuacao(nome, dificuldade, tentativas, True)
                break
        except ValueError:
            print("⚠️ Digite um número válido.")

    else:
        print(f"💥 Você perdeu! O número era {numero_secreto}.")
        salvar_pontuacao(nome, dificuldade, tentativas, False)

if __name__ == "__main__":
    jogo_adivinhacao()
