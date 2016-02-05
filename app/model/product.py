import shopify

class Product(object):
    def get_list(self):
        products = shopify.Product.find()
        print products
        return products