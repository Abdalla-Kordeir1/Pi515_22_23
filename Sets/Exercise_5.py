# A rival food truck approaches! Find out how the menus compare!

ourMenu = {'Pizza', 'Hot Dog', 'PB&J', 'Salad', 'Water', 'Soda'}
rivalMenu = {'Pasta', 'Pizza', 'Salad', 'Water', 'Soda'}

# 1. Find if the menu is different

print('Is Different?: ', ourMenu.isdisjoint(rivalMenu)  )

# 2. Find the unique items on our menu

print('Our Unique: ', ourMenu.difference(rivalMenu))

# 3. Find the unique items on the rival menu

print('Rival Unique: ', rivalMenu.difference(ourMenu))

# 4. Find all differences from both menus

print('All differences: ',ourMenu.symmetric_difference(rivalMenu))

# 5. Find common items between the menus

print('Common items: ', ourMenu.intersection(rivalMenu))

# 6. We want our food truck to be unique!! Make a new menu with only the uniqe items from both menus. Make sure to save the old menu in case our rival leaves! (Has many answers)

print('Old menu: ', ourMenu)
print('New menu: ', ourMenu.difference(rivalMenu).union(rivalMenu.difference(ourMenu)) )
