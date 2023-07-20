class ShoppingCart:
    def __init__(self, max_size) -> None:
        self.items: list[str] = []
        self.max_size = max_size

    def add_item(self, item: str) -> None:
        if self.get_size() == self.max_size:
            raise OverflowError(f"You cannot add more than {self.max_size} items.")
        self.items.append(item)

    def get_size(self) -> int:
        return len(self.items)

    def get_items(self) -> list[str]:
        return self.items

    def get_total_price(self, price_map):
        total = 0
        for item in self.items:
            total += price_map.get(item)
        return total