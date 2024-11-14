## Universidade Federal do Rio Grande do Norte - UFRN
## Centro de Ensino Superior do Seridó - CERES
## Departamento de Computação e Tecnologia - DCT
## Curso: Bacharelado em Sistemas de Informação
## Disciplina: DCT2102 – Redes de Computadores
## Professor: João Borges
## Alunos: Annielly Ferreira de Sousa, Fábio Fabricio Souza de Araújo
# <br/> Projeto e Implementação do Protocolo de Aplicação - Network Server Information Protocol (NSIP)

## Informações do Projeto
Este repositório contém a implementação de um cliente e servidor que utilizam o protocolo Network Server Information Protocol (NSIP) para a disciplina DCT2102 – Redes de Computadores na Universidade Federal do Rio Grande do Norte.

**Instituição**: Universidade Federal do Rio Grande do Norte - UFRN  
**Centro**: Centro de Ensino Superior do Seridó - CERES  
**Departamento**: Departamento de Computação e Tecnologia - DCT  
**Curso**: Bacharelado em Sistemas de Informação  
**Disciplina**: DCT2102 – Redes de Computadores  
**Professor**: João Borges  
**Data**: 11 de novembro de 2024  

## Descrição do Protocolo NSIP
O protocolo NSIP permite que um cliente obtenha informações sobre o status e o funcionamento de um servidor remoto. Este protocolo utiliza o modelo de comunicação cliente/servidor e é implementado sobre o protocolo de transporte UDP, utilizando a porta 2102.

### Formato do Pacote NSIP
O pacote NSIP é estruturado da seguinte forma:

| Campo     | Tamanho     | Descrição |
|-----------|-------------|-----------|
| **ID**    | 8 bits      | Identificador da consulta, utilizado tanto na requisição quanto na resposta |
| **TYPE**  | 8 bits      | Define o tipo de pacote: 0 - Requisição, 1 - Resposta, 2 - Erro |
| **CHECKSUM** | 16 bits  | Campo para verificação de erros |
| **QUERY** | 16 bits     | Tipo da consulta realizada |
| **RESULT** | 48 bytes   | Resultado da consulta, preenchido apenas na resposta |

### Tipos de Consulta (Campo QUERY)
O servidor NSIP pode responder às seguintes consultas:

- **SYS_PROCNUM** [0x0]: Número de processos em execução
- **SYS_BOOTIME** [0x1]: Tempo que o servidor está ligado
- **CPU_COUNT** [0x2]: Número de CPUs do servidor
- **CPU_PERCT** [0x3]: Porcentagem de uso da CPU
- **CPU_STATS** [0x4]: Estatísticas da CPU (context switches e interrupções)
- **MEM_TOTAL** [0x5]: Memória total
- **MEM_FREE** [0x6]: Memória disponível
- **MEM_PERCT** [0x7]: Porcentagem de uso da memória
- **DISK_PARTS** [0x8]: Lista de partições de disco
- **DISK_USAGE** [0x9]: Utilização das partições
- **NET_IFACES** [0x10]: Lista de interfaces de rede
- **NET_IPS** [0x11]: Lista de IPs das interfaces de rede
- **NET_MACS** [0x12]: Lista de MACs das interfaces de rede
- **NET_TXBYTES** [0x13]: Bytes enviados
- **NET_RXBYTES** [0x14]: Bytes recebidos
- **NET_TXPACKS** [0x15]: Pacotes enviados
- **NET_RXPACKS** [0x16]: Pacotes recebidos
- **NET_TCPCONS** [0x17]: Portas TCP abertas
- **NET_TCPLIST** [0x18]: Lista das portas TCP
- **NET_UDPCONS** [0x19]: Portas UDP abertas
- **NET_UDPLIST** [0x20]: Lista das portas UDP

### Cálculo do Checksum
O campo `CHECKSUM` é calculado somando todos os 54 bytes do pacote e aplicando módulo 216. O valor inicial do campo `CHECKSUM` deve ser 0 durante o cálculo.

```python
checksum = (sum(Bi for Bi in pacote_bytes)) % 216
```

### Ferramentas Utilizadas
- **Python psutil**: Para coleta de informações do sistema (ex.: processos, CPU, memória).

### Arquivos Disponibilizados
O arquivo `nsip.py`, que contém o cabeçalho dos pacotes e funções utilitárias, deve ser incluído no projeto tanto no cliente (`cliente.py`) quanto no servidor (`servidor.py`).

### Estrutura do Repositório
- **cliente.py**: Implementação do cliente NSIP.
- **servidor.py**: Implementação do servidor NSIP.
- **nsip.py**: Cabeçalho do protocolo e funções utilitárias para manipulação dos pacotes NSIP.

### Como Executar
1. Clone o repositório e acesse a pasta do projeto.
2. Execute o servidor:
   ```bash
   python servidor.py
   ```
3. Em outra janela de terminal, execute o cliente:
   ```bash
   python cliente.py
   ```

### Observações Importantes
- A atividade deve ser feita em dupla ou individual.
- Plágio resultará em nota 0 (zero) para ambos os grupos envolvidos.
- O trabalho deve ser submetido via SIGAA até a data estabelecida.
