#!/bin/bash

read -p "Enter Target IP: " ip
read -p "Enter NSE Script Name: " script

echo "Running Nmap Scan..."

nmap --script=$script $ip