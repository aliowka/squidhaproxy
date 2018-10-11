#!/usr/bin/env bash
rm myCA.pem
openssl genrsa -out myCA.key 1024
openssl req -new -key myCA.key -out myCA.csr
openssl x509 -req -days 365 -in myCA.csr -signkey myCA.key -out myCA.crt
cat myCA.crt myCA.key > myCA.pem