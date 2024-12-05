import socket
import sys

def scan(host, ports):
    try:
        # Iterando sobre as portas fornecidas
        for port in ports:
            # Criando o socket
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)  # Definindo o tempo limite para 1 segundo

            try:
                # Tentando conectar ao host e porta
                code = client.connect_ex((host, port))

                if code == 0:
                    print(f"[+] Porta {port} está ABERTA")
                else:
                    print(f"[-] Porta {port} está FECHADA")
            except socket.error as err:
                print(f"Erro ao conectar na porta {port}: {err}")
            finally:
                client.close()  # Fechar a conexão com o socket

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    # Entrada do Host (IP ou domínio)
    host = input("Digite o Host que deseja escanear (ex: google.com): ")

    # Entrada das portas específicas ou portas padrão
    port_input = input("Digite as portas específicas que deseja escanear (separadas por vírgula), ou aperte Enter para escanear as portas padrão: ")

    if port_input:
        # Converte a entrada em uma lista de inteiros
        ports = [int(p) for p in port_input.split(",")]
    else:
        # Lista de portas padrão
        ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]

    print(f"Iniciando escaneamento em {host} para as portas: {', '.join(map(str, ports))}")
    scan(host, ports)
