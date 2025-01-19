# Princípios SOLID em Python

Este repositório contém exemplos práticos dos princípios SOLID implementados em Python. Cada arquivo demonstra um princípio específico com exemplos de código "ruim" (violando o princípio) e "bom" (seguindo o princípio).

## Princípios Demonstrados

### S - Single Responsibility Principle (SRP)
- Arquivo: `single-responsability.py`
- Demonstra como uma classe deve ter apenas uma razão para mudar
- Exemplo de separação de responsabilidades entre gerenciamento de usuários e serviço de email

### O - Open/Closed Principle (OCP)
- Arquivo: `ocp.py`
- Mostra como as entidades de software devem estar abertas para extensão, mas fechadas para modificação
- Implementação de diferentes métodos de pagamento usando classes abstratas

### L - Liskov Substitution Principle (LSP)
- Arquivo: `liskov.py`
- Ilustra como as subclasses devem ser substituíveis por suas classes base
- Exemplo prático usando diferentes tipos de pássaros

### I - Interface Segregation Principle (ISP)
- Arquivo: `isp.py`
- Demonstra como interfaces grandes devem ser divididas em interfaces menores e mais específicas
- Exemplo usando dispositivos multifuncionais

### D - Dependency Inversion Principle (DIP)
- Arquivo: `dip.py`
- Mostra como módulos de alto nível não devem depender de módulos de baixo nível
- Exemplo de implementação de conexão com banco de dados usando abstração

## Como Usar

Cada arquivo contém dois exemplos:
1. Um exemplo "ruim" que viola o princípio
2. Um exemplo "bom" que segue o princípio

Os comentários no código explicam o contexto e as razões para as implementações.

## Contribuindo

Sinta-se à vontade para contribuir com mais exemplos ou melhorar os existentes através de pull requests.
