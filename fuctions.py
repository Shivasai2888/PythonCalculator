
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('country')} {kwargs.get('city')} {kwargs.get('zip')}")


shipping_label("GOAT!1", "CRISTIANO", "RONALDO", "1!",
               street="123",
               pobox="Pobox #27",
               city="manchester united",
               country="portugal",
               zip="968")
