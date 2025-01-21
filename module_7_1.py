class Product:
  def __init__(self, name, weight, category):
      self.name = name
      self.weight = weight
      self.category = category

  def __str__(self):
      return f'{self.name}, {self.weight}, {self.category}'


class Shop:
  __file_name = 'products.txt'

  def get_products(self):
      try:
          with open(self.__file_name, 'r') as file:
              return file.read()
      except FileNotFoundError:
          return "Файл не найден."

  def add(self, *products):
      existing_products = self.load_existing_products()

      for product in products:
          i = (product.name, product.category)
          if i in existing_products:
              # Если продукт уже есть, увеличиваем его вес
              existing_weight = existing_products[i]
              new_weight = existing_weight + product.weight
              existing_products[i] = new_weight
              print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_weight}.')
          else:
              # Если продукта нет, добавляем его в файл
              existing_products[i] = product.weight
              with open(self.__file_name, 'a') as file:
                  file.write(str(product) + '\n')

  def load_existing_products(self):
      products = {}
      try:
          with open(self.__file_name, 'r') as file:
              for line in file:
                  name, weight, category = line.strip().split(', ')
                  products[(name, category)] = float(weight)
      except FileNotFoundError:
          pass  # Если файл не найден, возвращаем пустой словарь
      return products


# Пример использования
if __name__ == "__main__":

  s1 = Shop()
  p1 = Product('Potato', 50.5, 'Vegetables')
  p2 = Product('Spaghetti', 3.4, 'Groceries')
  p3 = Product('Potato', 5.5, 'Vegetables')

  s1.add(p1, p2, p3)

  print(s1.get_products())
