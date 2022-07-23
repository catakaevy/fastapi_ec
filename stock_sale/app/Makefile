
.PHONY: appbuild
appbuild:       
	uvicorn main:app --reload

.PHONY: appb
appb:
	python3 -m uvicorn main:app

.PHONY: 1apil
1apil:
	curl -v -d '{"name": "test", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks

.PHONY: 1apiln
1apiln: 
	curl -v -d '{"name": "aiueo", "amount": None}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks

.PHONY: 1apilt
1apilt: 1apil
	curl -v -d '{"name": "aiueo", "amount": 10}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks

.PHONY: 1apile
1apile:
	curl -v -d '{"name": "aiueo", "amount": 10.0}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks

.PHONY: 1apile2
1apile2:
	curl -v -d '{"name": "aiueo", "amount": "abe"}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks

.PHONY: 2apil1
2apil1:
	curl http://localhost:8000/v1/stocks/test

.PHONY: 2apil2
2apil2: 2apil1
	curl http://localhost:8000/v1/stocks/no_stock

.PHONY: 2apilt
2apilt: 2apil2
	curl http://localhost:8000/v1/stocks

.PHONY: 3apil
3apil:
	curl -v -d '{"name": "test", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales

.PHONY: 3apil2
3apil2:
	curl -v -d '{"name": "float", "amount": 100, "price": 10}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales

.PHONY: 3apil3
3apil3:
	curl -v -d '{"name": "hoge", "amount": 100, "price": 10.123}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales

.PHONY: 3apil4
3apil4:
	curl -v -d '{"name": "hoge2", "amount": 100, "price": 10.1234}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales

.PHONY: 4apil
4apil:
	curl http://localhost:8000/v1/sales

.PHONY: 5apil
5apil: 
	curl -X DELETE http://localhost:8000/v1/stocks

.PHONY: test1
test1: 
	curl -v -d '{"name": "test", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks
	curl -v -d '{"name": "test", "amount": 10, "price": 10}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales
	curl http://localhost:8000/v1/stocks/test

.PHONY: ltest
ltest:
	curl -X DELETE http://localhost:8000/v1/stocks
	curl -v -d '{"name": "aiueo", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks
	curl -v -d '{"name": "aiueo", "amount": 10}' -H 'Content-Type: application/json' http://localhost:8000/v1/sales
	curl http://localhost:8000/v1/stocks/aiueo
	curl -v -d '{"name": "test", "amount": 100}' -H 'Content-Type: application/json' http://localhost:8000/v1/stocks
	curl http://localhost:8000/v1/stocks

	

