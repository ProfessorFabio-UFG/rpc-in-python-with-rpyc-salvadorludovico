import rpyc
from constRPYC import SERVER, PORT

print("=" * 70)
print("======= SEJA BEM VINDO AO SISTEMA DE CALCULADORA REMOTA DA AWS =======")
print("=" * 70)
print("\nOPERAÇÕES DISPONÍVEIS:")
print("-" * 70)
print("   🧮 SOMA:         add a b c ... z")
print("   ➖ SUBTRAÇÃO:    subtract a b c ... z")
print("   ✖️ MULTIPLICAÇÃO: multiply a b c ... z")
print("   ➗ DIVISÃO:      divide a b c ... z")
print("-" * 70)
print("Se cansar, digite 'exit' e eu prometo que vou desligar. 🚪👋")
print("=" * 70)

conn = rpyc.connect(SERVER, PORT)

def user_input_loop(conn):
    while True:
        data = input("Digite sua mensagem (ou 'exit' para sair): ")
        if data.lower() == "exit":
            print("Saindo...")
            break
        result = conn.root.handle_command(data)
        print("Resultado:", result)

user_input_loop(conn)
conn.close()
