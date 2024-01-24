#!/bin/bash

instances=$1
shift
ports=("$@")


if [ $instances != ${#ports[@]} ]; then
    echo "The number of instances and the number of ports must be the same."
    exit 1
fi

for ((i=0; i<$instances; i++))
do
    jolie service.ol --bindingPort ${ports[i]} &
done

