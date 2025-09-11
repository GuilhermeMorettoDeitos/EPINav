# EPINav
Software de controle de empréstimos de Equipamento de Proteção Individual (At. Desenvolvimento de Sistemas SENAI)

---

## 📋 Pré-requisitos

Antes de começar, verifique se você tem instalado em sua máquina:

- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) (se for rodar via container)

---

## 🚀 Passo a passo de instalação

### 1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/GuilhermeMorettoDeitos/EPINav.git
cd EPINav
````

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

#### 2.4 Criar superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

#### 2.5 Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 3. Rodando via Docker (recomendado)

#### 3.1 Construir a imagem Docker

No diretório raiz do projeto (onde está o Dockerfile), rode:

```bash
docker build -t epinav .
```

#### 3.2 Rodar o container

```bash
docker run -p 8000:8000 epinav
```

Isso iniciará o servidor do Django dentro do container, acessível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### 3.3 Acessar o sistema com usuário universal

* **Usuário:** `admin`
* **Senha:** `1234`

> Esse usuário já está pré-carregado via fixture para facilitar testes iniciais.

### 4. Rodando via Docker Compose

No diretório raiz do projeto:

```bash
docker-compose up --build
```

---

## 🤝 Colaboração

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adicionei nova feature'`)
4. Faça push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request 🚀