from classes.StardewValuer import StardewValuer
from data.data import items
from data.data import stars

inventory = StardewValuer('./inventories/in3.png')
inventory.find_items(items)
# inventory.detect_stars(stars)
inventory.display_results()