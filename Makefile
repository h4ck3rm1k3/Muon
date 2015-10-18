
#testcreate:
#	python3.4 src/muon2 mikes@createcafe.net
fire:
	python3.4 src/muon3 h4ck3rm1k3@identi.ca

test:
	#- rm ~/.muon
	#- rm ~/.config/PyPump/credentials.json
	#strace -f -eopen

	python3.4 src/muon2 h4ck3rm1k3@identi.ca

test2:
	- rm ~/.muon
	python3.4 src/muon h4ck3rm1k3@identi.ca
