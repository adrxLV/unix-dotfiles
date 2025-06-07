#!/bin/bash

#NOT NEEDED RN
# Obtém os dados do sistema
cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}' | cut -d. -f1)
mem=$(free | grep Mem | awk '{print int($3/$2 * 100)}')
disk=$(df / | grep / | awk '{print int($5)}')

# Atualiza as variáveis no EWW
eww update cpu_usage=$cpu
eww update mem_usage=$mem
eww update disk_usage=$disk
