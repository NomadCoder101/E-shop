from decimal import Decimal

from store.models import Product


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey') #'test'
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        # if 'test' not in request.session:
        #     basket = self.session['test'] = {}
            
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):

        """
          Colect the product ids in the session data to query the database 
        and eturn the products.
        """
        prdouct_ids =self.basket.keys()
        products =Product.products.filter(id__in=prdouct_ids)
        basket =self.basket.copy()

        for product in products:
            basket[str(product.id)]['product']= product
        
        for item in basket.values():
            item['price'] =Decimal(item['price'])
            item['total_price'] =item['price'] *  item['qty']
            yield item



    def __len__(self):

        """
        Get the basket data and count the quantity of items.
        """
        return sum(item['qty'] for item in self.basket.values())
    

    def get_total_price(self):

        """
        """
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
    
    
    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()
    

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
        self.save()

    def save(self):

        self.session.modified = True
