#!/bin/bash

for file in *.png ; do 
   basename=$(tr '[:lower:]' '[:upper:]' <<< "${file%.*}")
   newname="$basename.${file#*.}"
   mv "$file" "$newname"
done