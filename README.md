# Projeto Kafka + Spark com Docker
### Descrição do Projeto
Este projeto demonstra como configurar um ambiente Docker para criar um pipeline simples que utiliza o Apache Kafka para enviar números para o Apache Spark Structured Streaming. O Spark processará os números recebidos em tempo real e realizará cálculos básicos sobre eles.

### Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

### Configuração
1. Clone este repositório para o seu ambiente local:
```bash
git clone https://github.com/zycki-gif/spark-kafka-docker.git
```
2. Navegue até o diretório do projeto:
```bash
cd projeto-kafka-spark-docker
```
3. Inicie os serviços do Docker usando Docker Compose:
``` bash
docker-compose up -d
```
Aguarde até que os contêineres estejam prontos e em execução.
