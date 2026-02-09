# EPINav
Software de controle de empréstimos de Equipamento de Proteção Individual (At. Desenvolvimento de Sistemas SENAI)

---

## 📋 Pré-requisitos

Antes de começar, verifique se você tem instalado em sua máquina:

- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) (se for rodar via container)

---

### 1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/GuilhermeMorettoDeitos/EPINav.git
cd EPINav
```

---

### 2. Rodando localmente com Python

#### 2.1 Criar e ativar um ambiente virtual (venv)

##### Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

##### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate
```

> Sempre que for rodar o projeto, lembre-se de ativar o `venv`.

#### 2.2 Instalar dependências

```bash
pip install -r requirements.txt
```

#### 2.3 Configurar o banco de dados

```bash
python manage.py migrate
```

#### 2.4 Criar usuário padrão (obrigatório, se não estiver usando Docker)

```bash
python manage.py criar_usuarios_padrao
```

> Isso cria automaticamente o usuário `admin` com senha `1234` e o colaborador `colaborador1` com senha `1234`.

#### 2.5 Criar superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

#### 2.6 Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 3. Rodando via Docker

#### 3.1 Criar usuário padrão (obrigatório, se não estiver usando Docker)

```bash
python manage.py criar_usuarios_padrao
```

#### 3.2 Construir a imagem Docker

No diretório raiz do projeto (onde está o Dockerfile), rode:

```bash
docker build -t epinav .
```

#### 3.3 Rodar o container

```bash
docker run -p 8000:8000 epinav
```

Isso iniciará o servidor do Django dentro do container, acessível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### 3.4 Acessar o sistema com usuários padrão

* **UsuárioSistema:** `admin`
* **Senha:** `1234`

* **Colaborador:** `colaborador1`
* **Senha:** `1234`

> Esses usuários já estão pré-carregados via comando `criar_usuarios_padrao` para facilitar testes iniciais.
