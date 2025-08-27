# Desenvolvendo-um-Sistema-de-Cadastro-de-Produtos-em-Python-intermediario- # 🛒 Mini Sistema de Cadastro de Produtos em Python

![Python Logo](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📄 Descrição do Projeto

Este é um mini-projeto desenvolvido em Python para simular um sistema básico de cadastro e gerenciamento de produtos. O objetivo principal foi aplicar e integrar diversas estruturas de dados fundamentais do Python (`list`, `dict`, `tuple`, `set`) para resolver desafios comuns em aplicações de gerenciamento de dados, como a prevenção de duplicidade de itens e a validação de entradas.

O sistema permite ao usuário cadastrar novos produtos de forma interativa, garantindo a integridade dos dados através de validações robustas.

## ✨ Funcionalidades

-   **Cadastro Interativo:** Permite ao usuário inserir nome, preço e categoria de novos produtos via console.
-   **Prevenção de Duplicidade:** Utiliza um `set` para garantir que não haja produtos com nomes repetidos no catálogo.
-   **Validação de Categorias:** As categorias dos produtos são validadas contra uma lista pré-definida (`tuple`), aceitando apenas tipos válidos.
-   **Tratamento de Erros:** Implementa `try-except` para lidar com entradas inválidas (ex: preço não numérico), proporcionando uma experiência de usuário mais robusta.
-   **Armazenamento Estruturado:** Os produtos são armazenados em uma `list` de `dict`s, facilitando a organização e o acesso às informações.
-   **Exibição Detalhada:** Ao final do cadastro, exibe uma lista formatada de todos os produtos registrados.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.x:** Linguagem de programação principal.
-   **Estruturas de Dados:**
    -   `list`: Para a coleção principal de produtos.
    -   `dict`: Para representar cada produto com suas propriedades (nome, preço, categoria).
    -   `tuple`: Para definir as categorias válidas (imutáveis).
    -   `set`: Para um controle eficiente de nomes de produtos já cadastrados (prevenção de duplicidade).

## 🚀 Como Rodar o Projeto

1.  
    ```bash
    git clone [https://github.com/henriquedossantosduarte/Desenvolvendo-um-Sistema-de-Cadastro-de-Produtos-em-Python-intermediario-/edit/main/README.md]
    cd mini-sistema-cadastro-produtos
    ```
  

2.  **Execute o script Python:**
    ```bash
    python exercicio3.py
    ```

3.  **Siga as instruções no console:**
    O programa irá solicitar o nome, preço e categoria de cada produto. Você poderá cadastrar quantos produtos desejar e o sistema fará as validações automaticamente.

## 💡 Aprendizados e Destaques

Este projeto foi uma excelente oportunidade para:
-   Aprofundar a compreensão sobre a aplicação prática de `listas`, `dicionários`, `tuplas` e `conjuntos` em um cenário real.
-   Praticar a escrita de funções modulares e reutilizáveis.
-   Implementar lógica de validação de dados e tratamento de exceções (`try-except`) para criar um software mais resiliente.
-   Desenvolver um fluxo de interação com o usuário via console.

## 🤝 Contribuição

Sinta-se à vontade para explorar o código, sugerir melhorias ou reportar issues. Toda contribuição é bem-vinda!

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
*(Se você não tiver um arquivo LICENSE, pode remover esta seção ou criar um.)*

---
**Desenvolvido por:** [Seu Nome Completo]
**LinkedIn:** [Link para o seu perfil do LinkedIn]
**GitHub:** [Link para o seu perfil do GitHub]
