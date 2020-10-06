"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
def print_melon():
    """Print each melon with corresponding attribute information."""
 # create a big dictinary containing dictionary and a set for melong and attributes

    merged_dict = {}
    for key,value in melon_names.items():
        price = melon_prices.get(key, 0)
        seedless = melon_seedlessness.get(key, False)
        merged_dict[value.upper()] = [price, seedless]
    
    for key, value in merged_dict.items():
        name = key
        price = value[0]
        seedless = value[1]

        have_or_have_not = 'have'
        if seedless:
            have_or_have_not = 'do not have'

        print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
        # print(f"{key}: {value}")
    
    
print_melon()