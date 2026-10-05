<div align="center">

# 🇧🇷 THIS PROJECT IS AVAILABLE ONLY IN BRAZILIAN PORTUGUESE BECAUSE IS A STUDY PROJECT. 🇧🇷

<br>

# 🎬 CineClássico

### Landing Page de Locadora Física

*"O Prazer de Escolher o Filme na Prateleira Voltou."*

<br>

[![Site](https://img.shields.io/badge/🌐_Site_publicado-ver_online-e50914?style=for-the-badge)](https://felipe2008pg1.github.io/locadora_fisica/)
[![Status](https://img.shields.io/badge/status-publicado-success?style=for-the-badge)](https://felipe2008pg1.github.io/locadora_fisica/)
[![Projeto](https://img.shields.io/badge/projeto-de_estudo-blueviolet?style=for-the-badge)](#-criadores-do-projeto)

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=flat-square&logo=githubpages&logoColor=white)

</div>

---

## 📑 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Demonstração](#-demonstração)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#️-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Base de Dados do Acervo](#-base-de-dados-do-acervo-funcoes_dadospy)
- [Como Executar](#-como-executar-localmente)
- [Contato](#️-contato--redes-sociais)
- [Criadores](#-criadores-do-projeto)

---

## 🎞️ Sobre o Projeto

O **CineClássico** é uma landing page moderna, elegante e responsiva criada para promover a experiência nostálgica e autêntica de frequentar uma locadora de filmes física.

Em uma era dominada por algoritmos de streaming, o projeto resgata o valor de **garimpar prateleiras**, **folhear capas físicas** de mídia (Blu-ray, DVD e VHS) e **trocar recomendações de cinema** com quem entende do assunto.

> 🔗 **Acesse agora:** <https://felipe2008pg1.github.io/locadora_fisica/>

---

## 📸 Demonstração

<div align="center">

| Seção Principal | Categorias de Acervo |
| :---: | :---: |
| [![Hero Banner](img/demo/hero.png)](img/demo/hero.png) | [![Categorias](img/demo/categorias.png)](img/demo/categorias.png) |

| Como Funciona | Localização e Contato |
| :---: | :---: |
| [![Passo a Passo](img/demo/como-funciona.png)](img/demo/como-funciona.png) | [![Onde Estamos](img/demo/localizacao.png)](img/demo/localizacao.png) |

</div>

---

## 🚀 Funcionalidades

### 🎥 Landing Page

- **Hero Banner Nostálgico:** apresentação de impacto visual com tema escuro e clima de sala de cinema, com destaques numéricos (+10.000 títulos físicos, diária acessível e 100% amor ao cinema).
- **Catálogo Interativo:** listagem do acervo com contador de títulos encontrados e preço padrão da locação (R$ 4,90 / 48h).
- **Ordenação do Acervo:** mais recentes primeiro, mais antigos primeiro, ordem alfabética (A-Z) e (Z-A).
- **Cesta de Locação:** adicione filmes à cesta, acompanhe o total estimado para 48h e conclua a reserva na loja.
- **Detalhes do Filme:** ficha com mídia física (Blu-ray), diária de locação, áudio e legendas e status no estoque.
- **Explore por Segmentos:** prateleiras de *Fantasia & Clássicos*, *Ação & Aventura*, *Ficção Científica* e *Animação & Família*.
- **Como Funciona a Locação:** guia em 3 etapas (visita, cadastro rápido e locação por 48h).
- **Localização e Horários:** seção "Venha Tomar um Café Conosco!" com endereço, horário de funcionamento, contatos e atalho para o GPS. O mapa é um espaço reservado (placeholder).
- **Navegação Fluida:** menu superior com links diretos para cada seção, contador da cesta e botão de chamada para ação (*CTA*).

### 🐍 Script em Python

- **Organização do Catálogo:** agrupa os filmes por segmento e exibe o total de títulos de cada categoria diretamente no terminal.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso no projeto |
| :--- | :--- |
| ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) | Estruturação semântica da página |
| ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) | Estilização própria (sem frameworks): tema escuro, paleta vermelho e preto inspirada no cinema clássico, layout responsivo com Flexbox/Grid e rolagem suave via `scroll-behavior` |
| ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | Catálogo interativo, ordenação e cesta de locação |
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Base de dados do acervo e agrupamento por segmento (`funcoes_dados.py`) |
| ![Google Fonts](https://img.shields.io/badge/-Google_Fonts-4285F4?style=flat-square&logo=googlefonts&logoColor=white) | Tipografia: **Poppins** e **Bebas Neue** |
| ![Font Awesome](https://img.shields.io/badge/-Font_Awesome-528DD7?style=flat-square&logo=fontawesome&logoColor=white) | Ícones da interface |
| ![GitHub Pages](https://img.shields.io/badge/-GitHub_Pages-222222?style=flat-square&logo=githubpages&logoColor=white) | Publicação do site |

---

## 📂 Estrutura do Projeto

```
locadora_fisica/
├── 📁 img/
│   ├── 📁 demo/
│   │   ├── hero.png
│   │   ├── categorias.png
│   │   ├── como-funciona.png
│   │   └── localizacao.png
│   ├── 📁 acao/
│   ├── 📁 animacao/
│   ├── 📁 comedia;drama;suspense/
│   ├── 📁 fantasia/
│   └── 📁 ficcao/
├── 📁 locadora_fisica/
├── 📄 index.html
├── 🎨 style.css
├── 🐍 funcoes_dados.py
└── 📘 README.md
```

---

## 🗄️ Base de Dados do Acervo (`funcoes_dados.py`)

Script em Python puro (sem dependências externas) com a lista de **50 filmes** do acervo. Cada filme é um dicionário com `titulo`, `ano` e `segmento`:

```python
{"titulo": "Interestelar", "ano": 2014, "segmento": "Ficção Científica"}
```

A função `separar_e_exibir(catalogo)` agrupa os títulos por segmento e imprime o total de cada categoria.

| Segmento | Títulos |
| :--- | :---: |
| 💥 Ação | 15 |
| 🚀 Ficção Científica | 11 |
| 🧸 Animação | 10 |
| 🧙 Fantasia | 10 |
| 🎭 Comédia/Drama | 3 |
| 🎬 Drama/Suspense | 1 |
| **Total** | **50** |

**Exemplo de saída no terminal:**

```
=== CATÁLOGO DA LOCADORA SEPARADO POR SEGMENTO ===

[AÇÃO] - Total: 15 filmes
 • Vingadores: Ultimato (2019)
 • Spider-Man: No Way Home (2021)
 ...
----------------------------------------
```

---

## 💻 Como Executar Localmente

**1. Clone o repositório:**

```bash
git clone https://github.com/felipe2008pg1/locadora_fisica.git
```

**2. Acesse a pasta do projeto:**

```bash
cd locadora_fisica
```

**3. Abra a landing page:**

Abra o arquivo `index.html` no navegador de sua preferência, ou utilize a extensão **Live Server** no VS Code.

**4. (Opcional) Execute o script de catálogo:**

```bash
python funcoes_dados.py
```

> Requer Python 3.6+ (uso de f-strings).

---

## ✉️ Contato & Redes Sociais

| | |
| :--- | :--- |
| 📍 **Endereço** | Rua do Cinema, 420 - Bairro Central |
| ⏰ **Funcionamento** | Segunda a Sábado, das 10h às 20h |
| 📸 **Instagram** | [@cineclassico.locadora](https://instagram.com/cineclassico.locadora) |

---

## 👥 Criadores do Projeto

Projeto desenvolvido por:

<div align="center">

| 🎬 Felipe | 🎬 Nitay | 🎬 José | 🎬 Gracielli |
| :---: | :---: | :---: | :---: |

</div>

---

<div align="center">

*Feito com paixão pelo cinema de rua.* 🍿

⭐ Se gostou do projeto, deixe uma estrela no repositório!

</div>