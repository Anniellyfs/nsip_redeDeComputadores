import socket  # Importa o módulo socket para comunicação em rede
import psutil  # Importa psutil para monitoramento do sistema
from nsip import *  # Importa todas as definições do módulo NSIP

def nsip_server():
    # Cria um socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Servidor fica em loop, aguardando requisições
    server_address = ('localhost', 2102)
    print(f"Iniciando o servidor NSIP em {server_address}")
    server_socket.bind(server_address)

    # Servidor fica em loop, aguardando requisições
    while True:
        print('Aguardando uma conexão')
        data, address = server_socket.recvfrom(NSIP_LEN) # Recebe dados do cliente

        # Cria um pacote NSIP a partir dos dados recebidos
        req_packet = NSIPPacket()
        req_packet.from_packet(data)

        # Verifica se o pacote é uma requisição
        if req_packet.type == NSIP_REQ:
            print(f"Solicitação NSIP recebida com ID {req_packet.id} and QUERY {req_packet.query}")

            # Processa a requisição e gera a resposta
            result = process_nsip_query(req_packet.query)
            resp_packet = NSIPPacket(req_packet.id, NSIP_REP, req_packet.query, result)
            resp_packet.checksum = checksum(resp_packet.to_packet()) # Calcula e adiciona o checksum

            # Envia a resposta de volta ao cliente
            server_socket.sendto(resp_packet.to_packet(), address)
        else:
            print("Tipo de pacote NSIP inválido") # Informa erro para pacotes inválidos

def process_nsip_query(query):
    # Processa a consulta NSIP com base no tipo da query
    if query == SYS_PROCNUM:
        return str(len(psutil.process_iter())) # Retorna o número de processos ativos
    elif query == SYS_BOOTIME:
        return format_uptime(psutil.boot_time()) # Retorna o tempo desde a inicialização do sistema
    elif query == CPU_COUNT:
        return str(psutil.cpu_count()) # Retorna a contagem de CPUs
    elif query == CPU_PERCT:
        return f"{psutil.cpu_percent():.2f}" # Retorna o uso da CPU em percentual
    elif query == CPU_STATS:
        # Retorna contagem de trocas de contexto e interrupções
        ctx_switches = psutil.cpu_stats().ctx_switches
        interrupts = psutil.cpu_stats().interrupts
        return f"{ctx_switches},{interrupts}"
    # Adicione mais manipulação de consultas para outras queries conforme necessário
    else:
        return "Invalid query" # Retorna mensagem de erro para consultas desconhecidas

def format_uptime(boot_time):
    # Calcula o tempo desde a inicialização e o formata como dias, horas, minutos e segundos
    uptime = int(time.time() - boot_time)
    days = uptime // 86400
    hours = (uptime % 86400) // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60
    return f"{days}d {hours}h {minutes}m {seconds}s" # Retorna o uptime formatado

# Executa o servidor NSIP
if __name__ == "__main__":
    nsip_server()