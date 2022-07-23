.PHONY: login
login:
	ssh -i ./ec2 ec2-user@35.77.200.90  

# .PHONY: login2
# login2:
# 	ssh -i ./ec2 ec2-user@3.112.59.31

.PHONY: scp
scp:
	scp -i ./ec2 -r ec2-user@35.77.200.90:/home/ec2-user/fastapi/app .
	scp -i ./ec2 -r ec2-user@35.77.200.90:/home/ec2-user/kadai_log .
.PHONY: c1
c1:
	curl http://3.112.59.31:8000

# curl -v -d '{"name": "test", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks