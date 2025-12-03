# IsCoolGPT - Cloud Native AI Tutor

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Microservice-lightgrey?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Automated-2088FF?style=for-the-badge&logo=github-actions)
![Render](https://img.shields.io/badge/Deploy-Render-black?style=for-the-badge&logo=render)

> **Projeto Final da Disciplina de Cloud Computing**
> Uma aplicação Cloud-Native que utiliza Inteligência Artificial para atuar como um assistente universitário virtual, integrada com uma esteira completa de DevOps.

---

## Sobre o Projeto

O **IsCoolGPT** é uma API RESTful desenvolvida para auxiliar estudantes a compreenderem tópicos complexos de computação. Diferente de um chat comum, o sistema utiliza **Engenharia de Prompt** avançada no backend para assumir a "persona" de um **Professor Sênior**, devolvendo respostas estruturadas com:
1.  Definições Simples
2.  Analogias do Mundo Real
3.  Exemplos Práticos na Nuvem
4.  Casos de Uso de Negócio

### Diferenciais Técnicos
* **Arquitetura Cloud-Native:** Aplicação totalmente containerizada com Docker, garantindo portabilidade entre ambientes de desenvolvimento e produção.
* **LLM Agnostic:** Arquitetura desacoplada no módulo `services`, permitindo troca fácil entre modelos de IA (atualmente utilizando **Google Gemini**).
* **DevOps Culture:** Pipeline de CI/CD robusto com testes automatizados, verificação de estilo (linting) e promoção automática de código entre ambientes.
* **High Availability:** Deploy com estratégia **Zero Downtime** no Render (PaaS), garantindo que o serviço nunca saia do ar durante atualizações.

---

## Tech Stack

* **Linguagem:** Python 3.11
* **Framework Web:** Flask (Microframework)
* **Servidor de Produção:** Gunicorn (WSGI HTTP Server)
* **Inteligência Artificial:** Google Gemini API
* **Containerização:** Docker & Docker Compose
* **Testes & Qualidade:** Pytest (Testes Unitários com Mocking) & Flake8 (Linter)
* **CI/CD:** GitHub Actions
* **Cloud Provider:** Render (PaaS)

---

## Arquitetura de DevOps e Fluxo de Branches

Este projeto implementa uma estratégia avançada de gerenciamento de código e ambientes, automatizada via GitHub Actions:

### 1. Development (`development`)
* **Propósito:** Ambiente de desenvolvimento ativo.
* **Automação (CI):** A cada push ou commit manual, o pipeline `pipeline.yml` é acionado.
* **Checks:** Executa testes unitários (`pytest`) e linter (`flake8`). O build do Docker só ocorre se os testes passarem.

### 2. Staging (`staging`)
* **Propósito:** Ambiente de pré-produção (Gatekeeper).
* **Fluxo:** Recebe Pull Requests da branch `development`.
* **Deploy Automático:** Se os testes passarem, o pipeline `deploy.yml` faz o deploy na URL de Staging do Render.
* **Promoção Automática:** Se o deploy em Staging for bem-sucedido, o sistema abre e mergeia automaticamente um PR para a branch `main`, sem intervenção humana.

### 3. Main / Production (`main`)
* **Propósito:** Ambiente de Produção (Live).
* **Fluxo:** Idealmente recebe apenas código validado vindo de `staging`.
* **Hotfix Strategy:** O pipeline é inteligente para detectar emergências. Se um commit for feito diretamente na `main` (Hotfix), o script pula as etapas de Staging e Promoção e realiza o deploy imediato em Produção.

---

## Como Rodar Localmente

### Pré-requisitos
* Git
* Docker e Docker Compose instalados
* Uma chave de API do Google AI Studio (Gemini)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/EstelaLacerda/IsCoolGPT---Cloud-Project.git](https://github.com/EstelaLacerda/IsCoolGPT---Cloud-Project.git)
    cd IsCoolGPT---Cloud-Project
    ```

2.  **Configure a Segurança:**
    Crie um arquivo `.env` na raiz do projeto (este arquivo é ignorado pelo Git para segurança) e adicione sua chave:
    ```env
    GOOGLE_API_KEY="Sua_Chave_Aqui"
    ```

3.  **Execute com Docker (Recomendado):**
    Não é necessário instalar Python ou libs localmente. O Docker cuida de tudo.
    ```bash
    docker-compose up --build
    ```
    O servidor iniciará em `http://localhost:5000`.

---