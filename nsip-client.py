import socket
from nsip import * # Importa todos os elementos do módulo nsip (contendo definições de pacote NSIP)

def nsip_client():
    # Cria o UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor
    server_address = ('localhost', 2102)

    # Dicionário com consultas NSIP e seus IDs correspondentes
    queries = {
        'SYS_PROCNUM': SYS_PROCNUM, 
        'SYS_BOOTIME': SYS_BOOTIME,
        'CPU_COUNT': CPU_COUNT,
        'CPU_PERCT': CPU_PERCT,
        'CPU_STATS': CPU_STATS,
        'MEM_TOTAL': MEM_TOTAL,
        'MEM_FREE': MEM_FREE,
        'MEM_PERCT': MEM_PERCT,
        'DISK_PARTS': DISK_PARTS,
        'DISK_USAGE': DISK_USAGE,
        'NET_IFACES': NET_IFACES,
        'NET_IPS': NET_IPS,
        'NET_MACS': NET_MACS,
        'NET_TXBYTES': NET_TXBYTES,
        'NET_RXBYTES': NET_RXBYTES,
        'NET_TXPACKS': NET_TXPACKS,
        'NET_RXPACKS': NET_RXPACKS,
        'NET_TCPCONS': NET_TCPCONS,
        'NET_TCPLIST': NET_TCPLIST,
        'NET_UDPCONS': NET_UDPCONS,
        'NET_UDPLIST': NET_UDPLIST
    }

    # Define a consulta a ser enviada
    query = 'CPU_PERCT'
    query_id = queries[query]

    # Cria o pacote de requisição NSIP
    req_packet = NSIPPacket(1, NSIP_REQ, query_id, "")
    req_packet.checksum = checksum(req_packet.to_packet()) # Calcula e define o checksum

    # Envia a consulta ao servidor
    print(f"Enviando solicitação NSIP para {query}...")
    client_socket.sendto(req_packet.to_packet(), server_address)

    # Recebe a resposta do servidor
    data, _ = client_socket.recvfrom(1024) # Recebe até 1024 bytes de dados
    reply_packet = NSIPPacket()
    reply_packet.from_packet(data) # Converte os dados recebidos para um pacote NSIP

    # Processa a resposta recebida
    if reply_packet.type == NSIP_REP:
        print(f"Recebeu resposta do NSIP para {query}: {reply_packet.result}")
    elif reply_packet.type == NSIP_ERR:
        print(f"NSIP erro: {reply_packet.result}")
    else:
        print("Tipo de pacote NSIP inválido.")

    # Fecha o socket
    client_socket.close()

# Executa o cliente NSIP
if __name__ == "__main__":
    nsip_client()