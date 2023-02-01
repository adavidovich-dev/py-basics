#!/bin/bash
pip install "$1"
requirement_item=$(pip freeze | grep "$1")
if grep -Fxq "$requirement_item" requirements.txt
then
  echo "Requirement has been already added to requirements file"
else
  echo "$requirement_item" >> requirements.txt
  git commit -m "Add library: '$requirement_item'"
fi
