# Função para cadastrar um novo paciente
def cadastrar_paciente(pacientes):
   nome = input("Digite o nome do paciente: ")
   idade = int(input("Digite a idade do paciente: "))
   # Adicione mais campos conforme necessário
   novo_paciente = {"Nome": nome, "Idade": idade}
   pacientes.append(novo_paciente)
   print("Paciente cadastrado com sucesso!")
# Função para visualizar o prontuário de um paciente
def visualizar_prontuario(pacientes):
   nome_busca = input("Digite o nome do paciente: ")
   for paciente in pacientes:
       if paciente["Nome"].lower() == nome_busca.lower():
           print("Prontuário do Paciente:")
           for chave, valor in paciente.items():
               print(f"{chave}: {valor}")
           return
   print("Paciente não encontrado.")
# Função para atualizar informações de um paciente
def atualizar_paciente(pacientes):
   nome_busca = input("Digite o nome do paciente a ser atualizado: ")
   for paciente in pacientes:
       if paciente["Nome"].lower() == nome_busca.lower():
           print("Atualize as informações do paciente:")
           for chave in paciente.keys():
               novo_valor = input(f"{chave} ({paciente[chave]}): ")
               paciente[chave] = novo_valor if novo_valor != "" else paciente[chave]
           print("Informações do paciente atualizadas com sucesso!")
           return
   print("Paciente não encontrado.")
# Lista para armazenar pacientes
lista_pacientes = []
# Loop principal do programa
while True:
   # Solicitar ao usuário que indique se é médico, atendente ou paciente
   tipo_usuario = input("Digite 'm' para médico, 'a' para atendente ou 'p' para paciente: ")
   # Verificar o tipo de usuário e fazer login específico
   if tipo_usuario.lower() == 'm':
       while True:
           opcao = input("Escolha uma opção (1-4): \n 1- Cadastrar Paciente \n 2- Visualizar Prontuario \n 3- Atualizar Paciente \n 4- Fechar Programa\n")
           if opcao == "1":
               cadastrar_paciente(lista_pacientes)
           elif opcao == "2":
               visualizar_prontuario(lista_pacientes)
           elif opcao == "3":
               atualizar_paciente(lista_pacientes)
           elif opcao == "4":
               print("Saindo do programa. Até logo!")
               break
           else:
               print("Opção inválida. Por favor, escolha uma opção válida.")
       continue
   elif tipo_usuario.lower() == 'a':
       while True:
           opcao = input("Escolha uma opção (1-4):\n 1- Cadastrar Paciente \n 2- Visualizar Prontuario \n 3- Atualizar Paciente \n 4- Fechar Programa\n")
           if opcao == "1":
               cadastrar_paciente(lista_pacientes)
           elif opcao == "2":
               visualizar_prontuario(lista_pacientes)
           elif opcao == "3":
               atualizar_paciente(lista_pacientes)
           elif opcao == "4":
               print("Saindo do programa. Até logo!")
               break
           else:
               print("Opção inválida. Por favor, escolha uma opção válida.")
   elif tipo_usuario.lower() == 'p':
       while True:
           opcao = input("Escolha uma opção (2 ou 4):\n 2- Visualizar Prontuario \n 4- Fechar Programa\n")
           if opcao == "2":
               visualizar_prontuario(lista_pacientes)
           elif opcao == "4":
               print("Saindo do programa. Até logo!")
               break
           else:
               print("Opção inválida. Por favor, escolha uma opção válida.")
   else:
       print("Tipo de usuário inválido. Encerrando o programa.")
