from classes.StardewValuer import StardewValuer
from data.data import items
from data.data import stars

colors = {
    'silver': ([0, 0, 180], [180, 30, 255]),
    'gold': ([20, 100, 100], [30, 255, 255]),
    'iridium': ([120, 50, 50], [160, 255, 255])
}

inventory = StardewValuer('./inventories/in3.png')
inventory.find_items(items)
inventory.find_stars(colors)
inventory.display_results()