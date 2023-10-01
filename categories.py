class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

class CategoryManager:
    def __init__(self):
        self.categories = []
        self.next_category_id = 1

    def add_category(self, name):
        category =Category(self.next_category_id, name)
        self.categories.append(category)
        self.next_category_id += 1

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category.category_id == category_id:
                category.name = new_name
                break

    def get_all_categories(self):
        return self.categories
    
    