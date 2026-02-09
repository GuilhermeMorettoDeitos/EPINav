#!/bin/sh
set -e
python manage.py migrate
python manage.py criar_usuarios_padrao
echo "Iniciando servidor..."
echo "Acesse aqui: http://localhost:8000"
exec "$@"
