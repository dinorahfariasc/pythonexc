# # Estatísticas de times de futebol
# class Time(object):

#     def __init__(self, nome, golsM, golsS):
#         self.nome = nome
#         self.golsM = golsM
#         self.golsS = golsS


# def golsMarcados(time):
#     return time.golsM


# qntd = int(input("Digite a quantidade de times: "))

# times = []

# for i in range(qntd):
#     nome = input("Digite o nome do time: ")
#     golsM = int(input("Digite o número de gols marcados: "))
#     golsS = int(input("Digite o número de gols sofridos: "))
#     time = Time(nome, golsM, golsS)
#     times.append(time)  

# # ordenar a lista de times por gols marcados
# times.sort(key=golsMarcados, reverse=True)


# for i in range(qntd):
#     print(f"{i+1} - {times[i].nome}\nGols Marcados: {times[i].golsM}\nGols Sofridos: {times[i].golsS}")

#=========================================================================================================
#  Compra de Smartphone

# class Smartphone(object):

#     def __init__(self, modelo, memoria, processador, camera, bateria):
#         self.modelo = modelo
#         self.memoria = memoria
#         self.processador = processador
#         self.camera = camera
#         self.bateria = bateria

#     def tabela(self):
#         print(f"Modelo: {self.modelo}\nMemoria: {self.memoria}GB\nProcessador: {self.processador}Ghz\nCamera: {self.camera}Pixels\nBateria: {self.bateria}mA")


# # entrada de dados

# entrada = ''
# catalogo = []

# while True:
#     entrada = input()
#     if(entrada == 'n'):
#         memoriaTeste = int(input('memoria minima:'))
#         processadorTeste = float(input('processador minimo:'))
#         cameraTeste = float(input('camera minima: '))
#         bateriaTeste = float(input('bateria minima: '))
#         break
    
#     elif(entrada == 's'):
#         modelo = input('modelo: ')
#         memoria = int(input('memoria:'))
#         processador = float(input('processador:'))
#         camera = float(input('camera: '))
#         bateria = float(input('bateria:'))
#         smartphone = Smartphone(modelo, memoria, processador, camera, bateria)
#         catalogo.append(smartphone)

# count = 0
# for celular in catalogo:
#     if(celular.memoria >= memoriaTeste and celular.processador >= processadorTeste and celular.camera >= cameraTeste and celular.bateria >= bateriaTeste):
#         celular.tabela()
#         print('\n')
#         count += 1

# print(f"{count} smartphone encontrados.") if count > 0 else print("0 smartphones encontrados")
       
#=========================================================================================================
# bola pro mato (tabela times de futebol pontos corridos)

# class Time(object):
    
#         def __init__(self, nome, vitorias, empates, derrotas, golsM, golsS):
#             self.nome = nome
#             self.vitorias = vitorias
#             self.empates = empates
#             self.derrotas = derrotas
#             self.golsM = golsM
#             self.golsS = golsS
#             self.pontos = (self.vitorias * 3) + self.empates
#             self.jogos = self.vitorias + self.empates + self.derrotas
    
#         def tabela(self):
#             print(f"{self.nome}| {self.pontos}| {self.jogos}| {self.vitorias}| {self.empates}| {self.derrotas}| {self.golsM}| {self.golsS}")

# def ordenarTimes(time):
#     return time.pontos

# qntd = int(input("Digite a quantidade de times: "))
# times = []

# for i in range(qntd):
#     nome = input("Digite o nome do time: ")
#     vitorias = int(input("Digite o número de vitórias: "))
#     empates = int(input("Digite o número de empates: "))
#     derrotas = int(input("Digite o número de derrotas: "))
#     golsM = int(input("Digite o número de gols marcados: "))
#     golsS = int(input("Digite o número de gols sofridos: "))
#     time = Time(nome, vitorias, empates, derrotas, golsM, golsS)
#     times.append(time)

# times.sort(key=ordenarTimes, reverse=True)
# rebaixados = times[-4:]
# liberta = times[:6]

# print("Nome| Pontos| Jogos| Vitórias| Empates| Derrotas| Gols Marcados| Gols Sofridos")
# for i in range(qntd):
#     times[i].tabela()

# print("\nTimes na zona da Libertadores:")
# for i in range(6):
#     print(f"{liberta[i].nome}")

# print("\nTimes rebaixados:")
# for i in range(4):
#     print(f"{rebaixados[i].nome}")

#=========================================================================================================

#CRUD   
# class Pessoa(object):

#     def __init__(self, nome, idade, sexo):
#         self.nome = nome
#         self.idade = idade
#         self.sexo = sexo


# def cadastrarPessoa():
#     nome = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade da pessoa: "))
#     sexo = input("Digite o sexo da pessoa: ")
#     pessoa = Pessoa(nome, idade, sexo)
#     return pessoa

# def deletarPessoa(lista):
#     nome = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade da pessoa: "))
#     sexo = input("Digite o sexo da pessoa: ")

#     for pessoa in lista:
#         if nome == pessoa.nome and idade == pessoa.idade and sexo == pessoa.sexo:
#             lista.remove(pessoa)

#     return lista

# def imprimirPessoas(lista):
#     for pessoa in lista:
#         print(f"{pessoa.nome}, {pessoa.idade} ,{pessoa.sexo}")


# cadastros = []

# while True:
#     comando = input("Digite o comando: ")
#     if comando == 'p':
#         break
#     elif comando == 'i':
#         pessoa = cadastrarPessoa()
#         cadastros.append(pessoa)
#     elif comando == 'd':
#         cadastros = deletarPessoa(cadastros)

# imprimirPessoas(cadastros)
#=========================================================================================================