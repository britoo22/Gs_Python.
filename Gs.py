# Função para exibir o menu
def exibir_menu():
    print("Sistema de Prontuário Médico - Menu")
    print("1. Cadastrar paciente")
    print("2. Visualizar prontuário")
    print("3. Atualizar informações do paciente")
    print("4. Sair")

# Função para realizar o login do médico
def fazer_login_medico():
    # Hardcoded para simplicidade, você pode implementar uma lógica mais segura
    crm_correto = "12345"
    senha_correta = "senha_medico"

    crm_digitado = input("Digite o CRM: ")
    senha_digitada = input("Digite a senha: ")

    if crm_digitado == crm_correto and senha_digitada == senha_correta:
        print("Login bem-sucedido! Bem-vindo, Médico.")
        return True
    else:
        print("CRM ou senha incorretos. Acesso negado.")
        return False

# Função para realizar o login do atendente
def fazer_login_atendente():
    # Hardcoded para simplicidade, você pode implementar uma lógica mais segura
    usuario_correto = "atendente"
    senha_correta = "senha_atendente"

    usuario_digitado = input("Digite o usuário: ")
    senha_digitada = input("Digite a senha: ")

    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print("Login bem-sucedido! Bem-vindo, Atendente.")
        return True
    else:
        print("Usuário ou senha incorretos. Acesso negado.")
        return False

# Função para realizar o login do paciente
def fazer_login_paciente():
    # Hardcoded para simplicidade, você pode implementar uma lógica mais segura
    numero_seguro_social_correto = "987654321"
    senha_correta = "senha_paciente"

    numero_seguro_social_digitado = input("Digite o número do seguro social: ")
    senha_digitada = input("Digite a senha: ")

    if numero_seguro_social_digitado == numero_seguro_social_correto and senha_digitada == senha_correta:
        print("Login bem-sucedido! Bem-vindo, Paciente.")
        return True
    else:
        print("Número do seguro social ou senha incorretos. Acesso negado.")
        return False

# Lista para armazenar pacientes
lista_pacientes = []

# Solicitar ao usuário que indique se é médico, atendente ou paciente
tipo_usuario = input("Digite 'm' para médico, 'a' para atendente ou 'p' para paciente: ")


def cadastrar_paciente(lista_pacientes):
    pass
def visualizar_prontuario(lista_pacientes):
    pass
def atualizar_paciente(lista_pacientes):
    pass

# Verificar o tipo de usuário e fazer login específico
if tipo_usuario.lower() == 'm':
    if fazer_login_medico():
        # Loop principal do programa para médicos
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção (1-4): ")

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

elif tipo_usuario.lower() == 'a':
    if fazer_login_atendente():
        # Loop principal do programa para atendentes
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção (1-4): ")

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
    if fazer_login_paciente():
        # Loop principal do programa para pacientes
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção (2 ou 4): ")

            if opcao == "2":
                visualizar_prontuario(lista_pacientes)
            elif opcao == "4":
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

else:
    print("Tipo de usuário inválido. Encerrando o programa.")
