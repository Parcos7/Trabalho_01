Trabalho 1 - Inventário de Ativos e Vulnerabilidades (Cibersegurança)

Este repositório contém o código-fonte desenvolvido para a 1ª Atividade Avaliativa da disciplina de Cibersegurança na Universidade Federal de Uberlândia (UFU).

O projeto consiste em um sistema de linha de comando em Python que simula uma base de inventário de segurança, permitindo realizar operações de CRUD (Criar, Consultar, Atualizar e Remover) em ativos de TI e suas respectivas vulnerabilidades.

🚀 Como Clonar o Repositório

Para baixar uma cópia deste repositório para o seu computador e executar o projeto localmente, siga os passos abaixo:

Pré-requisitos

Certifique-se de ter instalado em sua máquina:

Git

Python 3.x

Passo a Passo

Abra o terminal (Prompt de Comando, PowerShell ou Git Bash) no diretório onde deseja salvar o projeto.

Execute o comando de clonagem utilizando a URL do repositório:

git clone https://github.com/Parcos7/Trabalho_01.git


Entre na pasta criada pelo comando:

cd Trabalho_01


Execute o arquivo principal da aplicação utilizando o Python:

python main.py


🛠️ Tecnologias e Recursos Utilizados

Linguagem: Python

Controle de Versão: Git / GitHub (Utilização de múltiplas branches e operações de merge)

Persistência de Dados: Manipulação de arquivos locais em formato JSON.

Estruturas de Dados: Uso de dicionários (dict) otimizados como hash maps para buscas e a classe Enum para a tipagem dos ativos.

📋 Funcionalidades do Sistema

Menu Interativo: Interface textual via prompt com tratamento de exceções (try/except) para evitar falhas com entradas incorretas.

Gestão de Ativos (CRUD):

Cadastrar: Inserção de novos equipamentos (Notebook, Servidor, Roteador ou Banco de Dados) com ID numérico único.

Consultar: Busca indexada por ID ou hostname.

Atualizar: Modificação de dados cadastrais.

Remover: Exclusão de ativos e suas vulnerabilidades vinculadas.

Gestão de Vulnerabilidades: Inclusão contínua de fragilidades associadas aos ativos, com classificação de severidade e status de tratamento.
