#!/bin/bash

get_pid() {
    PID=$(pgrep -f server_connection.py)
    echo "Server PID: $PID"
}

kill_server() {
    PID=$(pgrep -f server_connection.py)
    if [ -z "$PID" ]; then
        echo "Server is not running."
    else
        echo "Killing server (PID: $PID)..."
        kill $PID
    fi
}

if [ "$1" == "get_pid" ]; then
    get_pid
elif [ "$1" == "kill_server" ]; then
    kill_server
else
    echo "Usage: $0 [get_pid | kill_server]"
fi
