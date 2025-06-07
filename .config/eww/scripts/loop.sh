#!/bin/bash

# Loop para atualizar os dados a cada 5 segundos
while true; do
  ~/.config/eww/scripts/update_metrics.sh
  sleep 5
done
