price = float(input('price='))
discount = int(input('discount='))
reduction = round(price*discount/100,2)
price_w_dsc = price-reduction
print(f'reduction {reduction}, price with reduction {price_w_dsc}')