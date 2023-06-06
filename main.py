from custom_modules.car_functions import import_car_brand

selected_brands = input("Choose a brand:\n")

selected_brands_list = selected_brands.split(" ")

for selected_brand in selected_brands_list:
    import_car_brand(selected_brand)