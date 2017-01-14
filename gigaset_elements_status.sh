#!/bin/sh

gigasetelements-cli -u "$1" -p "$2" | grep Status | sed 's/.*Modus .*\(HOME\|AWAY\).*/\1/'
