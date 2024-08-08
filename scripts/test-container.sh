#!/bin/sh

path_to_script () {
  if ! [ -L "$1" ]; then
    echo "$1"
  else
    path_to_script "$(readlink -f "$1")"
  fi
}

PTS=$(path_to_script "$0")
PD=$(readlink -f "$(dirname "${PTS}")/..")
COMPOSE_FILE="${PD}/tests/docker-compose.yml"
# echo "COMPOSE_FILE: ${COMPOSE_FILE}"

case "$1" in
  start)
    docker compose -p tdnsapilib -f "$COMPOSE_FILE" up -d
  ;;
  stop)
    docker compose -p tdnsapilib -f "$COMPOSE_FILE" stop
  ;;
  * )
    echo "usage: $(basename "$0" .sh) start|stop"
    exit 1
  ;;
esac

exit $?
