#!/bin/bash

if [ "$1" != "install" ] && [ "$1" != "uninstall" ]; then
  echo ERROR: Bad command \'"$1"\'
  exit 1
fi

if [ "$2" = "" ]; then
  echo ERROR: No any requirement has been provided
  exit 1
fi

case "$1" in
install)
  echo INFO: Installing \'"$2"\'...
  pip install "$2"
  requirement_descriptor=$(pip freeze | grep -i "$2")
  if [ "$requirement_descriptor" = "" ]; then
    echo "ERROR: Requirement has not been found"
    exit 1
  fi

  if grep -Fxq "$requirement_descriptor" requirements.txt; then
    echo "INFO: Requirement has been already added to requirements file"
  else
    echo "$requirement_descriptor" >>requirements.txt
    git commit -m "Add library: '$requirement_descriptor'"
  fi
  ;;
uninstall)
  echo Uninstalling \'"$2"\'...
  requirement_descriptor=$(pip freeze | grep -i "$2")
  if [ "$requirement_descriptor" = "" ]; then
    echo "ERROR: Requirement has not been found"
    exit 1
  fi
  pip uninstall "$2" --yes
  sed -i "/$requirement_descriptor/d" requirements.txt
  ;;
*)
  echo ERROR: unknown command "$1"
  ;;
esac

