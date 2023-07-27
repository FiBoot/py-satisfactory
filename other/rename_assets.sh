#!/bin/bash

for file in *.png ; do 
   mv "$file" "${file//_/ }";
   # basename=$(tr '[:lower:]' '[:upper:]' <<< "${file%.*}")
   # newname="$basename.${file#*.}"
   # mv "$file" "$newname"
done