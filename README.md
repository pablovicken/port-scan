# PortScanner 🧹
Este projeto é um scanner de portas simples, desenvolvido em Python, que permite verificar a disponibilidade de portas em um servidor ou dispositivo de rede. O PortScanner pode ser usado para realizar uma auditoria básica de segurança, identificar portas abertas e ajudar a proteger sistemas, sendo uma ferramenta útil para profissionais de cibersegurança.

## Objetivo 📌
O principal objetivo desse projeto é ajudar a realizar uma análise básica da exposição de portas em servidores e dispositivos. Usando um simples script em Python, o scanner tenta se conectar a um conjunto de portas especificadas e informa se a porta está aberta ou fechada. É uma ferramenta essencial para quem deseja aprender sobre cibersegurança, redes e testes de penetração (pentesting).

## Funcionalidades 🗂
Escaneamento de portas específicas: O script permite que o usuário insira portas específicas a serem escaneadas ou use um conjunto de portas padrão.
Entrada interativa: O script solicita ao usuário que informe o host (domínio ou IP) e as portas que deseja escanear.
Exibição de resultados: Informa se a porta está aberta ou fechada para cada porta fornecida.
Portas padrão: Caso o usuário não informe as portas, o script utiliza um conjunto de portas comuns (21, 22, 80, 443, etc.).

## Tecnologias Utilizadas 🔎
Python 3.x: Linguagem de programação principal usada para desenvolver o script.
Socket: Biblioteca padrão do Python usada para realizar a conexão com as portas do servidor.

## *Requisitos* 🔗
- Python 3.x instalado em seu sistema.

## Como Executar 📋
#### Passos para rodar o script

1- Clone o repositório para o seu computador:
```
git clone https://github.com/seuusuario/portscanner.git
```
2- Navegue até o diretório do projeto:
```
cd portscanner
```
3- Execute o script:
```
python portscan.py
```
*Quando solicitado, insira o host (domínio ou IP) que deseja escanear e as portas que deseja verificar. Caso não forneça portas, o script utilizará as portas padrão.*

## Exemplo de Execução 📊
```
Digite o Host que deseja escanear (ex: google.com): google.com
Digite as portas específicas que deseja escanear (separadas por vírgula), ou aperte Enter para escanear as portas padrão: 22,80,443
Iniciando escaneamento em google.com para as portas: 22, 80, 443
[+] Porta 22 está ABERTA
[+] Porta 80 está ABERTA
[+] Porta 443 está ABERTA
```
## Objetivo do Projeto
Este projeto foi desenvolvido com o objetivo de melhorar as minhas habilidades em cibersegurança e programação em Python, criando uma ferramenta simples e eficaz para escanear portas de servidores de rede. Além disso, é uma ótima maneira de entender como funcionam as conexões TCP e como podemos testar a disponibilidade de serviços em uma rede.


Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
