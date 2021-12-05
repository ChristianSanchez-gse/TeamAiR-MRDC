#!/bin/bash

cat $1 | awk '{print $1}'
cat $1 | awk '{print $2}'
