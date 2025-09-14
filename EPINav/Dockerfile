FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Copia o entrypoint e dá permissão de execução
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# Para Utilizar no Windows, descomente o bloco abaixo e comente o bloco acima

# FROM python:3.12

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8000

# # Garante que o script tenha LF e permissão
# COPY entrypoint.sh /entrypoint.sh
# RUN sed -i 's/\r$//' /entrypoint.sh && chmod +x /entrypoint.sh

# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

