# EPINav
Software de controle de empréstimos de Equipamento de Proteção Individual (At. Desenvolvimento de Sistemas SENAI)

---

## 📋 Pré-requisitos

Antes de começar, verifique se você tem instalado em sua máquina:

- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---

## 🚀 Passo a passo de instalação

### 1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/SEU_USUARIO/EPINav.git
cd EPINav
````

---

### 2. Criar e ativar um ambiente virtual (venv)

#### Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate
```

> Sempre que for rodar o projeto, lembre-se de ativar o `venv`.

---

### 3. Instalar dependências

Com o ambiente virtual ativado, rode:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar o banco de dados

Rodar as migrações iniciais:

```bash
python manage.py migrate
```

---

### 5. Criar um superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

Digite usuário, e-mail e senha.

---

### 6. Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Abra no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🤝 Colaboração

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adicionei nova feature'`)
4. Faça push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request 🚀
