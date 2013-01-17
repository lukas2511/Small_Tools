#!/bin/bash

ip="192.168.100.61"

while true
do
	read -s -n 1 realchar
	charnum=$(printf "%d" \'$realchar)
	if [ "$charnum" = "127" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Back' -d '{"jsonrpc":"2.0","method":"Input.Back","id":1}' -H 'Content-Type: application/json';
		echo
	fi
	if [ "$realchar" = "" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Select' -d '{"jsonrpc":"2.0","method":"Input.Select","id":1}' -H 'Content-Type: application/json'
		echo
	fi
	if [ "$realchar" = "A" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Up' -d '{"jsonrpc":"2.0","method":"Input.Up","id":1}' -H 'Content-Type: application/json'
		echo
	fi
	if [ "$realchar" = "B" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Down' -d '{"jsonrpc":"2.0","method":"Input.Down","id":1}' -H 'Content-Type: application/json'
		echo
	fi
	if [ "$realchar" = "C" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Right' -d '{"jsonrpc":"2.0","method":"Input.Right","id":1}' -H 'Content-Type: application/json'
		echo
	fi
	if [ "$realchar" = "D" ]
	then
		curl 'http://'$ip'/jsonrpc?Input.Left' -d '{"jsonrpc":"2.0","method":"Input.Left","id":1}' -H 'Content-Type: application/json'
		echo
	fi
done
