import jwt

"""
Para a pyJWT os algoritmos disponíveis são os na lista
https://pyjwt.readthedocs.io/en/stable/algorithms.html
"""

token = jwt.encode({"user": "felipe"}, "senha", algorithm="HS256")

print(token)

# Se não precisar verificar a assinatura
print(jwt.decode(token, options={"verify_signature": False}))

# Para verificar a assinatura com senha errada:
try:
    print("Tentando validar com a senha errada")
    print(jwt.decode(token, 'errada', algorithms=["HS256"]))
except jwt.InvalidSignatureError:
    print("A assinatura não pôde ser validada.")
# Com a senha está certa:
try:
    print("Tentando validar com a senha correta.")
    print(jwt.decode(token, 'senha', algorithms=["HS256"]))
except jwt.InvalidSignatureError:
    print("A assinatura não pôde ser validada.")

# As tokens podem ter validade, e uma claim registrada quem define isso.
# https://pyjwt.readthedocs.io/en/stable/usage.html#registered-claim-names
import datetime
import time

token_expira = jwt.encode({"user": "felipe", "exp": datetime.datetime.now(tz=datetime.timezone.utc)+datetime.timedelta(seconds=10)}, 'senha', algorithm="HS256")

# Quando a token não venceu
try:
    payload = jwt.decode(token_expira, "senha", algorithms=["HS256"])
    print(payload)
except jwt.ExpiredSignatureError:
    print("A token já havia vencido.")

# Quando a token venceu
try:
    print("Vamos demorar")
    time.sleep(11)
    payload = jwt.decode(token_expira, "senha", algorithms=["HS256"])
    print(payload)
except jwt.ExpiredSignatureError:
    print("A token já havia vencido.")