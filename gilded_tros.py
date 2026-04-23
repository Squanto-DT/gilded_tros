# -*- coding: utf-8 -*-

class GildedTros(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Never touch legendary item
            if item.name == "B-DAWG Keychain":
                continue
            
            item.sell_in -= 1
            # update quality
            if item.sell_in >= 0:
                self._update_quality_pre_sell_in(item)
            else:
                self._update_quality_post_sell_in(item)

    def _update_quality_pre_sell_in(self, item):
        if item.name == 'Good Wine' or 'Backstage passes' in item.name:
            self._increase_quality(item)
            if 'Backstage passes' in item.name and item.sell_in <= 10:
                self._increase_quality(item)
                if item.sell_in <= 5:
                    self._increase_quality(item)
        elif item.name in ["Duplicate Code", "Long Methods", "Ugly Variable Names"]:
            self._decrease_quality(item, 2)
        else:
            self._decrease_quality(item, 1)
        
    
    def _update_quality_post_sell_in(self, item):
        if item.name == 'Good Wine':
            self._increase_quality(item, 2)
        elif 'Backstage passes' in item.name:
            item.quality = 0
        elif item.name in ["Duplicate Code", "Long Methods", "Ugly Variable Names"]:
            self._decrease_quality(item, 4)
        else:
            self._decrease_quality(item, 2)

    def _increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
