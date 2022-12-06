# Create your order for the food truck and see if your order is available

menu = {'Pizza', 'Hot Dog', 'PB&J', 'Salad', 'Water', 'Soda'}

print('Order available :',{'Pizza', 'Hot Dog', 'Salad'}.issubset(menu))


# Make an order that isn't available

print("Order unavailable  :",{'Pizza', 'Chocolate', 'Ramen'}.issubset(menu))

