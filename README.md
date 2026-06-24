# Portfolio Web + Microserviço de Notificações

Projeto desenvolvido utilizando Django e Django REST Framework.

## Requisitos

- Python 3.12+
- Git
- Pip

---

## 1. Clonar os projetos

### Portfolio Web

```bash
git clone https://github.com/Dowglas-Hademar/Portfolio-Web-Update.git
```

### Microserviço de Notificações

```bash
git clone https://github.com/Dowglas-Hademar/Microservico-Notificacoes.git
```

---

## 2. Criar ambiente virtual

Entre na pasta do projeto:

```bash
cd Portfolio-Web-Update
```

Criar venv:

```bash
python -m venv venv
```

Ativar:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependências

No Portfolio:

```bash
pip install -r requirements.txt
```

No Microserviço:

```bash
pip install -r requirements.txt
```

---

## 4. Executar migrações

### Portfolio

```bash
python manage.py migrate
```

### Microserviço

```bash
python manage.py migrate
```

---

## 5. Criar usuário administrador

### Portfolio

```bash
python manage.py createsuperuser
```

### Microserviço

```bash
python manage.py createsuperuser
```

---

## 6. Configurar comunicação entre os sistemas

No arquivo `settings.py` do Portfolio:

```python
NOTIFICACAO_MS_URL = 'http://127.0.0.1:8001'
NOTIFICACAO_MS_API_KEY = 'SUA_API_KEY'
```

A API Key deve ser a mesma cadastrada na empresa criada no Microserviço.

---

## 7. Executar os projetos

### Microserviço

Abrir um terminal:

```bash
cd Microservico-Notificacoes
python manage.py runserver 8001
```

### Portfolio

Abrir outro terminal:

```bash
cd Portfolio-Web-Update
python manage.py runserver
```

---

## 8. Testando o sistema

### Acessar os admins

Microserviço:

```
http://127.0.0.1:8001/admin
```

Portfolio:

```
http://127.0.0.1:8000/admin
```

### Criar Empresa

No admin do Microserviço:

- Acesse Empresas
- Clique em Adicionar Empresa
- Informe o nome
- Salve

Será gerado um hash automaticamente.

Copie esse hash e coloque em:

```python
NOTIFICACAO_MS_API_KEY
```

do arquivo `settings.py` do Portfolio.

### Criar Notificação

Endpoint:

```http
POST /api/notificacoes/criar/
```

Exemplo:

```json
{
  "user_id": 1,
  "titulo": "Teste",
  "mensagem": "Notificação de teste"
}
```

Header:

```http
X-Api-Key: HASH_DA_EMPRESA
```

### Resultado esperado

Ao acessar o Portfolio com o usuário correspondente, a notificação deve aparecer no sino de notificações.

---

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite