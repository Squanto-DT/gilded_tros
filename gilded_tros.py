# -*- coding: utf-8 -*-

class GildedTros(object):

    def __init__(self, items):
        self.items = items

#
#    def update_quality(self):
#        for item in self.items:
#            if item.name != "Good Wine" and item.name != "Backstage passes for Re:Factor" \
#                    and item.name != "Backstage passes for HAXX":
#                if item.quality > 0:
#                    if item.name != "B-DAWG Keychain":
#                        item.quality = item.quality - 1
#            else:
#                if item.quality < 50:
#                    item.quality = item.quality + 1
#                    if item.name == "Backstage passes for Re:Factor" or item.name == "Backstage passes for HAXX":
#                        if item.sell_in < 11:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
#                        if item.sell_in < 6:
#                            if item.quality < 50:
#                                item.quality = item.quality + 1
#            if item.name != "B-DAWG Keychain":
#                item.sell_in = item.sell_in - 1
#            if item.sell_in < 0:
#                if item.name != "Good Wine":
#                    if item.name != "Backstage passes for Re:Factor" and item.name != "Backstage passes for HAXX":
#                        if item.quality > 0:
#                            if item.name != "B-DAWG Keychain":
#                                item.quality = item.quality - 1
#                    else:
#                        item.quality = item.quality - item.quality
#                else:
#                    if item.quality < 50:
#                        item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            # Never touch legendary item
            if item.name == "B-DAWG Keychain":
                continue
            
            item.sell_in -= 1
            # update quality
            self._update_quality_pre_sell_in(item)

            # check if sell in = 0
            if item.sell_in < 0:
                self._update_quality_post_sell_in(item)

    def _update_quality_pre_sell_in(self, item):
        # 'Normal' Item
        # 'Wine of backstage pass'
        if item.name == 'Good Wine' or 'Backstage Passes' in item.name:
            item.quality += 1
            if 'Backstage passes' in item.name and item.sell_in <= 10:
                item.quality += 1
                if item.sell_in <= 5:
                    item.quality += 1
        else:
            pass
        
    
    def _update_quality_post_sell_in(self, item):
        pass

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
