#Aqui vou dsenvolver meu código de teste para a revisão.

# Lista (array) para armazenar os motores em memória
motores = []

def cadastrar_motor():
    print("\n--- Cadastrar Novo Motor ---")
    codigo = input("Código/ID do motor: ").strip()
    
    # Verifica se o código já existe
    for motor in motores:
        if motor["codigo"] == codigo:
            print("Erro: Já existe um motor cadastrado com este código.")
            return

    marca = input("Marca (ex: WEG, Siemens): ").strip()
    potencia = input("Potência (ex: 5 CV, 10 HP): ").strip()
    tensao = input("Tensão (ex: 220V/380V): ").strip()
    rpm = input("Rotação (RPM): ").strip()

    motor = {
        "codigo": codigo,
        "marca": marca,
        "potencia": potencia,
        "tensao": tensao,
        "rpm": rpm
    }
    
    motores.append(motor)
    print(f"Motor '{codigo}' cadastrado com sucesso!")

def listar_motores():
    print("\n--- Lista de Motores Cadastrados ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for i, motor in enumerate(motores, start=1):
        print(f"{i}. Cód: {motor['codigo']} | Marca: {motor['marca']} | "
              f"Potência: {motor['potencia']} | Tensão: {motor['tensao']} | RPM: {motor['rpm']}")

def buscar_motor():
    print("\n--- Buscar Motor ---")
    codigo = input("Digite o código do motor: ").strip()
    
    for motor in motores:
        if motor["codigo"] == codigo:
            print("\nMotor encontrado:")
            print(f"  Código:   {motor['codigo']}")
            print(f"  Marca:    {motor['marca']}")
            print(f"  Potência: {motor['potencia']}")
            print(f"  Tensão:   {motor['tensao']}")
            print(f"  RPM:      {motor['rpm']}")
            return
            
    print("Motor não encontrado.")

def remover_motor():
    print("\n--- Remover Motor ---")
    codigo = input("Digite o código do motor a ser removido: ").strip()
    
    for i, motor in enumerate(motores):
        if motor["codigo"] == codigo:
            motores.pop(i)
            print(f"Motor '{codigo}' removido com sucesso!")
            return
            
    print("Motor não encontrado.")

def menu():
    while True:
        print("\n=== SISTEMA DE CADASTRO DE MOTORES ===")
        print("1. Cadastrar motor")
        print("2. Listar todos os motores")
        print("3. Buscar motor por código")
        print("4. Remover motor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()
