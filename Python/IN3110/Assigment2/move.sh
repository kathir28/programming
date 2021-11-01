#!/bin/bash
# Moves folder from source to destination
move () {
# Moves folder from source to destination
# Arguments:
#   - Sourcepath
#   - Destinationpath

# Output:
#   - None if succesfull
#   - Error message if un-successfull

  if [[ $# -ne 2 ]];
  #Checks if number of arguments are correct
  # If not , error message is echoed and function exits
  then
    echo "Input data is wrong, input is "./move.sh "src" "dest"
  fi

  src=$1
  dst=$2

  if [[ ! -d "$src" ]];
  # Checks if source path exits
  # If not , error message is echoed and function exits
  then
    echo "Source dictonary does not exist"
    exit
  fi

  if [[ ! -d "$dst" ]];
  # Checks if destination path exits
  # If not , error message is echoed and function exits
    then
      echo "Source dictonary does not exist"
      exit
    fi
  mv $src/* $dst
}
move $1 $2

