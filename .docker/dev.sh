#!/usr/bin/env bash
set -euo pipefail

_usage() {
  echo "Usage: dev [command]"
  echo ""
  echo "Commands:"
  echo "  pipi          Instale los requisitos de Python según los requirements.txt"
  echo "  migrate       Run migraciones"
  echo "  new_migration Crear una nueva migración con un nombre generado automáticamente"
  echo ""
  exit 1
}

# Show usage if no argument is given
if [[ $# -eq 0 ]]; then
  _usage
fi

# Command input
arg=${1:-}
shift || _usage

case ${arg} in
  pipi)
    echo "Instalando requirements..."
    pip install -r requirements.txt
  ;;
  migrate)
    echo "Corriendo migraciones..."
    alembic upgrade head
  ;;
  new_migration)
    read -p "Escribe un nombre para la migracion: " migration_name
    echo "Creando nueva migracion: $migration_name"
    alembic revision --autogenerate -m "$migration_name"
  ;;
  *)
    echo "Unknown command: ${arg}"
    _usage
  ;;
esac
