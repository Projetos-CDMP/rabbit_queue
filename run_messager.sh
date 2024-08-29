#!/bin/bash

counter=1

while true; do
    MESSAGE="Message $counter"
    MESSAGE="$MESSAGE" python queue_module/messager.py
    ((counter++))
    sleep 10
done