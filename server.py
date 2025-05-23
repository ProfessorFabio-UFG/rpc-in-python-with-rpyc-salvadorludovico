import rpyc
from rpyc.utils.server import ThreadedServer
from constRPYC import PORT

class CalculatorService(rpyc.Service):
    def exposed_handle_command(self, command_str):
        parts = command_str.strip().split()
        if not parts:
            return "Comando vazio."

        op = parts[0]
        args = list(map(int, parts[1:]))

        match op:
            case "add":
                return sum(args)
            case "subtract":
                return args[0] - sum(args[1:])
            case "multiply":
                result = 1
                for num in args:
                    result *= num
                return result
            case "divide":
                try:
                    result = args[0]
                    for num in args[1:]:
                        result /= num
                    return result
                except ZeroDivisionError:
                    return "Erro: divisão por zero."
            case _:
                return "Comando desconhecido."

if __name__ == "__main__":
    server = ThreadedServer(CalculatorService, port=PORT)
    print(f"Servidor RPyC ouvindo na porta {PORT}...")
    server.start()
