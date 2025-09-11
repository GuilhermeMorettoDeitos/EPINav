#!/bin/sh

echo "Rodando migrações..."
python manage.py migrate --noinput
python manage.py loaddata usuarios_iniciais.json || true


echo "Iniciando servidor..."
echo "Acesse aqui: http://localhost:8000"
exec "$@"
