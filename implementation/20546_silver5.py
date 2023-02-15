start = int(input())
price = [int(i) for i in input().split()]

bnp_cash = start
timing_cash = start

bnp_stock = 0
timing_stock = 0

timing_inc_count = 0
timing_dec_count = 0

for i in range(len(price)):
    #bnp buying case 
    if bnp_cash >= price[i]:
        bnp_stock += bnp_cash // price[i]
        bnp_cash %= price[i]
    #bnp finish

    #timing case
    if price[max(0,i-1)] < price[i]:
        timing_inc_count += 1
        timing_dec_count = 0
    elif price[max(0,i-1)] > price[i]:
        timing_dec_count += 1
        timing_inc_count = 0
    elif price[max(0,i-1)] == price[i]:
        timing_dec_count = 0
        timing_inc_count = 0
    
    #timing buy
    if(timing_dec_count >= 3):
        if timing_cash >= price[i]:
            timing_stock += timing_cash // price[i]
            timing_cash %= price[i]
    if(timing_inc_count >= 3):
        if timing_stock > 0:
            timing_cash += timing_stock * price[i]
            timing_stock = 0

bnp_result = bnp_cash + bnp_stock * price[len(price) - 1]
timing_result = timing_cash + timing_stock * price[len(price) - 1]

if(bnp_result > timing_result):
    print("BNP")
elif(bnp_result < timing_result):
    print("TIMING")
else:
    print("SAMESAME")