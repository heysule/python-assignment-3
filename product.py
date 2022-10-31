class Product:
  id = ''
  name =''
  price = ''
  image_url = ''
  quantity = 0
  is_stocked = False
  is_discounted = False
  discount = 0

  def __init__(self, name, price, quantity) -> None:
    self.name = name
    self.price = price
    self.quantity = quantity