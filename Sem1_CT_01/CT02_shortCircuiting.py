def bake_cookies(recipe):
    print("Baking Cookies:")
    
    if 'mixing' in recipe and recipe['mixing']:
        print("Step 1: Mix the ingredients.")

    if 'shaping' in recipe and recipe['shaping']:   # shortcircuited
        print("Step 2: Shape the cookie dough.")

    if 'baking' in recipe and recipe['baking']:
        print("Step 3: Bake the cookies.")

    if 'decorating' in recipe and recipe['decorating']:
        print("Step 4: Decorate the baked cookies.")

# Recipe
cookie_recipe = {
    'mixing': True,
    'shaping': False,  # Set it to false
    'baking': True,
    'decorating': True
}

bake_cookies(cookie_recipe)
