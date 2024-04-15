import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

class Aluno:
    def __init__(self, nome, ano, turma, data_nascimento, numero_aluno, nota):
        self.nome = nome
        self.ano = ano
        self.turma = turma
        self.data_nascimento = data_nascimento
        self.numero_aluno = numero_aluno
        self.nota = nota

class SistemaRegistroAlunos:
    def __init__(self):
        self.alunos = []
        self.estatisticas = defaultdict(dict)  # Dicionário para armazenar estatísticas por turma

    def adicionar_aluno(self):
        print("\nAdicionar Aluno")
        nome = input("Nome do aluno: ")
        ano = input("Ano do aluno: ")
        turma = input("Turma do aluno: ")
        data_nascimento = input("Data de Nascimento do aluno (AAAA-MM-DD): ")
        numero_aluno = input("Número do aluno: ")
        nota = float(input("Nota do aluno: "))
        aluno = Aluno(nome, ano, turma, data_nascimento, numero_aluno, nota)
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado com sucesso!")

    def remover_aluno(self):
        print("\nRemover Aluno")
        numero_aluno = input("Digite o número do aluno que deseja remover: ")
        for aluno in self.alunos:
            if aluno.numero_aluno == numero_aluno:
                self.alunos.remove(aluno)
                print(f"Aluno {aluno.nome} removido com sucesso!")
                return
        print("Aluno não encontrado.")

    def atualizar_informacoes_aluno(self):
        print("\nAtualizar Informações do Aluno")
        numero_aluno = input("Digite o número do aluno que deseja atualizar: ")
        for aluno in self.alunos:
            if aluno.numero_aluno == numero_aluno:
                nome = input(f"Novo nome para {aluno.nome}: ")
                ano = input(f"Novo ano para {aluno.nome}: ")
                turma = input(f"Nova turma para {aluno.nome}: ")
                data_nascimento = input(f"Nova data de nascimento para {aluno.nome} (AAAA-MM-DD): ")
                aluno.nome = nome if nome else aluno.nome
                aluno.ano = ano if ano else aluno.ano
                aluno.turma = turma if turma else aluno.turma
                aluno.data_nascimento = data_nascimento if data_nascimento else aluno.data_nascimento
                print(f"Informações do aluno {aluno.nome} atualizadas com sucesso!")
                return
        print("Aluno não encontrado.")

    def listar_alunos(self):
        print("\nLista de Alunos:")
        if not self.alunos:
            print("Não há alunos registrados.")
        else:
            for aluno in self.alunos:
                print(f"Nome: {aluno.nome}, Ano: {aluno.ano}, Turma: {aluno.turma}, Data de Nascimento: {aluno.data_nascimento}, Número de Aluno: {aluno.numero_aluno}")

    def calcular_estatisticas(self):
        if not self.alunos:
            print("Não há alunos registrados.")
            return

        notas_por_turma = defaultdict(list)
        for aluno in self.alunos:
            notas_por_turma[aluno.turma].append(aluno.nota)

        for turma, notas in notas_por_turma.items():
            media = np.mean(notas)
            mediana = np.median(notas)
            desvio_padrao = np.std(notas)
            self.estatisticas[turma] = {
                'média': media,
                'mediana': mediana,
                'desvio padrão': desvio_padrao
            }
            print(f"Estatísticas da Turma {turma}:")
            print(f"Média: {media:.2f}")
            print(f"Mediana: {mediana:.2f}")
            print(f"Desvio Padrão: {desvio_padrao:.2f}")
            print()

    def gerar_grafico(self):
        if not self.alunos:
            print("Não há alunos registrados.")
            return

        notas_por_turma = defaultdict(list)
        for aluno in self.alunos:
            notas_por_turma[aluno.turma].append(aluno.nota)

        for turma, notas in notas_por_turma.items():
            plt.hist(notas, bins=10, alpha=0.5, label=f"Turma {turma}")
        
        plt.xlabel('Notas')
        plt.ylabel('Frequência')
        plt.title('Distribuição de Notas por Turma')
        plt.legend(loc='upper right')
        plt.show()

# Função principal
def main():
    sistema = SistemaRegistroAlunos()

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Informações do Aluno")
        print("4. Listar Alunos")
        print("5. Calcular Estatísticas")
        print("6. Gerar Gráfico de Notas")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.adicionar_aluno()
        elif opcao == "2":
            sistema.remover_aluno()
        elif opcao == "3":
            sistema.atualizar_informacoes_aluno()
        elif opcao == "4":
            sistema.listar_alunos()
        elif opcao == "5":
            sistema.calcular_estatisticas()
        elif opcao == "6":
            sistema.gerar_grafico()
        elif opcao == "7":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()