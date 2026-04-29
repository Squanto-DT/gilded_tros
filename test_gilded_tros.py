# -*- coding: utf-8 -*-
import unittest

from gilded_tros import Item, GildedTros


class GildedTrosTest(unittest.TestCase):
    
    def test_normal_item_degrades(self):
        items = [Item(name="Ring of Cleansening Code", sell_in=10, quality=20)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_normal_item_degrades_twice_after_sell_in(self):
        items = [Item(name="Ring of Cleansening Code", sell_in=-2, quality=10)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_legendary_item_never_degrades(self):
        items = [Item("B-DAWG Keychain", 4, 80)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_good_wine_increases_in_quality(self):
        items = [Item(name="Good Wine", sell_in=2, quality=0)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_good_wine_increases_in_quality_after_sell_in(self):
        items = [Item(name="Good Wine", sell_in=-2, quality=0)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_backstage_passes_increase_in_quality_pre_sell_in_more_than_10_days(self):
        items = [Item(name="Backstage passes for Re:Factor", sell_in=15, quality=20)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_in_quality_pre_sell_in_less_than_10_days(self):
        items = [Item(name="Backstage passes for Re:Factor", sell_in=10, quality=20)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_in_quality_pre_sell_in_less_than_5_days(self):
        items = [Item(name="Backstage passes for Re:Factor", sell_in=5, quality=20)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_decrease_to_zero_after_sell_in(self):
        items = [Item(name="Backstage passes for Re:Factor", sell_in=-2, quality=20)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_smelly_items_decrease_in_quality_pre_sell_in(self):
        items = [Item(name="Long Methods", sell_in=3, quality=6)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_smelly_items_decrease_in_quality_post_sell_in(self):
        items = [Item(name="Long Methods", sell_in=-1, quality=6)]
        tros = GildedTros(items)
        tros.update_quality()
        self.assertEqual(2, items[0].quality)

if __name__ == '__main__':
    unittest.main()
