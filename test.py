import json


raw_data = '"[{\"order_symbol\":\"BTCUSD\",\"order_ticket\":202593157.00000000,\"close_price\":68519.04000000,\"order_closetime\":0.00000000,\"order_commission\":0.00000000,\"order_expiration\":0.00000000,\"order_lots\":0.10000000,\"order_magicNumber\":0.00000000,\"order_openPrice\":68433.70000000,\"order_openTime\":1730103059.00000000,\"order_profit\":8.53000000,\"order_stopLoss\":0.00000000,\"order_swap\":0.00000000,\"order_takeProfit\":0.00000000,\"order_type\":0.00000000},{\"order_symbol\":\"BTCUSD\",\"order_ticket\":202593081.00000000,\"close_price\":68519.04000000,\"order_closetime\":0.00000000,\"order_commission\":0.00000000,\"order_expiration\":0.00000000,\"order_lots\":0.10000000,\"order_magicNumber\":0.00000000,\"order_openPrice\":68451.58000000,\"order_openTime\":1730101531.00000000,\"order_profit\":6.75000000,\"order_stopLoss\":64379.20000000,\"order_swap\":0.00000000,\"order_takeProfit\":0.00000000,\"order_type\":0.00000000}]\u0000"'
data = json.loads(raw_data)

print(data)