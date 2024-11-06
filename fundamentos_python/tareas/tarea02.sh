#!/bin/bash
dir_name="Tarea02"
file_name="Ejercicio"
extension=".py"

mkdir $dir_name

for i in {1..8}
do
	touch $dir_name/$file_name"0"$i$extension
done
