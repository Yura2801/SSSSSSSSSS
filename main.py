from user_func import make_sale,load_products_from_file




sales_file = "sales_history.csv"
data_base_file = "data_base.csv"

products = load_products_from_file(data_base_file)

make_sale(sales_file, products)

