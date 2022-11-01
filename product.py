from abc import ABC, abstractmethod
import uuid

# Simulates database 
database = []

def findItem(id):
  for item in database:
    if (item.id == id):
      return item
      


class Product:
  id = ''
  name =''
  price = ''
  image_url = ''
  quantity = 0
  is_stocked = False
  is_discounted = False
  discount = 0

  def __init__(self, name: str, price: float, quantity: int) -> None:
    self.name = name
    self.price = price
    self.quantity = quantity


class ProductAbstract(ABC):
  """
  Abstract Class For Implementing Product Management

  Attributes
  ----------

  Methods
  -------
  create_product(product: Product)
    Creates a product

  edit_product(product_id: str, data: dict)
    Updates a product

  get_product_by_id(product_id: str)
    Fetches a product by id

  get_all_products()
    Fetches all products

  upload_product_image(product_id: str, product_image_url: str)
    Updates a products image

  delete_product(product_id: str)
    Deletes a product
  """

  @abstractmethod
  def create_product(self, product: Product):
    """
    Parameters
    ----------
    product: Product
      The product object being created
    """
    pass

  @abstractmethod
  def edit_product(self, product_id: str, data: dict):
    """
    Parameters
    ----------
    product_id: str
      The id of the product being updated
    data: dict
      The properties of the product to be updated
    """
    pass

  @abstractmethod
  def get_product_by_id(self, product_id: str):
    """
    product_id: str
      The id of the product being fetched
    """
    pass

  @abstractmethod
  def get_all_products(self):
    """
    Parameters
    ----------
    None
    """
    pass

  @abstractmethod
  def upload_product_image(self, product_id: str, product_image_url: str):
    """
    Parameters
    ----------
    product_id: str
      The id of the product being updated
    product_image_url: str
      A string containing the location of the image of the product
    """
    pass

  @abstractmethod
  def delete_product(self, product_id: str):
    """
    Parameters
    ----------
    product_id: str
      The id of the product being deleted
    """
    pass


class ProductManager(ProductAbstract):
  """
  A class that implements ProductAbstract
  """

  def create_product(self, product: Product):
    id = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    product.id = id

    if (product.quantity > 0):
      product.is_stocked = True

    database.append(product)

  def edit_product(self, product_id: str, data: dict):
    product = findItem(product_id)

    if (product):
      for key, value in data.items():
        setattr(product, key, value)

  def get_product_by_id(self, product_id: str):
    return findItem(product_id)

  def get_all_products(self):
    return database

  def upload_product_image(self, product_id: str, product_image_url: str):
    product = findItem(product_id)
    
    if (product):
      product.image_url = product_image_url

  def delete_product(self, product_id: str):
    product = findItem(product_id)

    if (product):
      database.remove(product)

