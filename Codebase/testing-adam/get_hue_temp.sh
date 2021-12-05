#!/bin/bash

cat $1 | grep Hue > $1
cat $1 | sed 's/Hue: //' | sed 's/, Temperature://' > $1
cat $1 | awk '{print $1}'
cat $1 | awk '{print $2}'
