class Category:

    def __init__(self,category_id,category_name):

        self.category_id=category_id
        self.category_name=category_name

    def display_category(self):

        print("Category ID:",self.category_id)
        print("Category Name:",self.category_name)