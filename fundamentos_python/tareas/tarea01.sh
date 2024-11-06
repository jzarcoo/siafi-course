#!/bin/bash
dir_name="Tarea01"
file_name="Ejercicio"
file_name_extra="Extra"
extension=".py"

mkdir $dir_name

for i in {1..10}
do
    if [ $i -lt 10 ]
    then
        touch $dir_name/$file_name"0"$i$extension
    else
        touch $dir_name/$file_name$i$extension
    fi
done

for i in {1..3}
do
    touch $dir_name/$file_name_extra"0"$i$extension
done