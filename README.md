# Simple mirror api 
Responds with request line, request headers and body as output.
Useful for seeing what client applications send

## Requirements
Python 3.9.6

## Config
Set port and whether to use SSL or not in server.py
A self signed cert is provided, you can replace it with actual cert and key

## Run
python3 server.py

Point http client to default url: http://localhost:8083/
![image](https://user-images.githubusercontent.com/5017434/124982556-af857600-dfeb-11eb-8f34-72a3967b7910.png)


demo cert/key PASSPHRASE: test
