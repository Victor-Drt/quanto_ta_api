## 🛠️ Comparador de Preços de Produtos (API)

API desenvolvida com Django REST Framework para registrar e comparar preços de produtos, com foco inicial em móveis. Usuários autenticados podem cadastrar produtos, registrar preços observados em lojas e consultar seus próprios registros.

> ⚠️ Este projeto está em desenvolvimento.
> Autenticação de usuários já implementada. Demais funcionalidades ainda estão sendo construídas.

---

### ✅ Funcionalidades atuais

* [x] Registro de usuários (cadastro via endpoint público)
* [x] Login/autenticação com token
* [x] Endpoint `/users/profile/` para consultar dados do usuário logado

---

### 🚧 Funcionalidades previstas

* Cadastro de produtos por usuário
* Registro de preços por produto e loja
* Cadastro de lojas e categorias
* Consulta e comparação dos preços registrados

---

### 🚀 Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* SQLite (temporário)
* Token Authentication (JWT)

---

### 📂 Organização prevista

* `products/`: app com modelos de Produto, Preço, Loja e Categoria
* `users/`: app com autenticação e controle de usuários

---

### 📌 Observações

Este repositório representa um projeto pessoal de aprendizado e organização. Sugestões e melhorias serão bem-vindas conforme o desenvolvimento avança.
