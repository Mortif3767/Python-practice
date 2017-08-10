width=input('please enter width:')
price_width=10
item_width=width-price_width
head_format='%-*s%*s'
format='%-*s%*.2f'
print '='*width
print head_format % (price_width,'Item',item_width,'Price')
print '-'*width
print format % (price_width,'Apple',item_width,0.5)
print format % (price_width,'Pineapple',item_width,3.5)
print format % (price_width,'Banana',item_width,0.9)