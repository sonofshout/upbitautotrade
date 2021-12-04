import pyupbit

access = "zT2cunu5lsGDxn9VbXOzJztGeZk7lHNkdxHOI7Tc"          # 본인 값으로 변경
secret = "vj3Ze8KOvc8qeMDixVISRfnJ39jKaYXdQgCBTbG9"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-ETH 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회