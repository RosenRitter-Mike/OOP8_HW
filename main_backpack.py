from CompositBag import CompositeBag
from LeafItem import LeafItem

backpack = CompositeBag("Large camping backpack")
healthy_bag = CompositeBag("Healthy food bag")
corn = LeafItem("Cob of corn", 0.3)

bread = LeafItem("Brioche bread", 0.5)
cheese = LeafItem("Brie cheese", 0.3)
snack_pack = CompositeBag("Snack pack")

bamba = LeafItem("Bamba Osem", 0.2)
bissli = LeafItem("Bissli onion", 0.2)
marshmallow = LeafItem("Marshmallows (Not roasted)", 0.3)
water = LeafItem("Large Perrier water bottle", 1)

snack_pack.add_item(bamba)
snack_pack.add_item(bissli)
snack_pack.add_item(marshmallow)
snack_pack.add_item(water)

healthy_bag.add_item(bread)
healthy_bag.add_item(cheese)
healthy_bag.add_item(snack_pack)

backpack.add_item(healthy_bag)
backpack.add_item(corn)

print("The weight of the backpack: ", backpack.get_weight())
