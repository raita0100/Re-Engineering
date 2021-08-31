#!/bin/sh
# Print the current working directory
echo "we are in : "
pwd

# Reading input from terminal
echo Enter your name
read name

echo welcome $name

# unsetting the variable
unset name
echo After unsetting : $name
