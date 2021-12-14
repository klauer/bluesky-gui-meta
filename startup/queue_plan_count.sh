#!/bin/bash

# source activate bsgui

echo "Opening the environment..."
qserver environment open
qserver queue clear

sleep 10

echo "Checking for allowed devices and plans..."
qserver allowed devices
qserver allowed plans

echo "Queuing a simple 'count' plan using 'motor1':"
qserver queue add plan '{"name": "count", "args": [["motor1"]], "kwargs": {"num": 10, "delay": 1}}'

echo "Running the queue..."
qserver queue start
