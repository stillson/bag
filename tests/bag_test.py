#!/usr/bin/env python

import bag
import unittest


class TestBagMethods(unittest.TestCase):

    def test_pop(self):
        # also test init...
        b = bag.Bag(1, 2, 3, 4)

        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))

    def test_push(self):
        b = bag.Bag()
        b.add(1)
        b.add(2)
        b.add(3).add(4)
        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))
        self.assertIn(b.pop(), (1, 2, 3, 4))

    def test_add(self):
        b1 = bag.Bag(1, 2, 3)
        b2 = bag.Bag(4, 5, 6)

        b3 = b1 + b2

        self.assertIn(1, b3)
        self.assertIn(4, b3)
        self.assertEqual(len(b3), 6)

    def test_iter(self):
        b = bag.Bag(1, 2, 3, 4, 5)

        l = list(b)
        l.sort()

        self.assertListEqual(l, [1, 2, 3, 4, 5])
        for i in b:
            self.assertIn(i, (1, 2, 3, 4, 5))

    def test_len(self):
        b = bag.Bag()

        self.assertEqual(len(b), 0)

        b.add(1)
        self.assertEqual(len(b), 1)

    def test_nz(self):
        b = bag.Bag()
        t1 = False
        t2 = False

        if b:
            t1 = True

        b.add(1)

        if b:
            t2 = True

        self.assertFalse(t1)
        self.assertTrue(t2)

    def test_repr(self):
        b = bag.Bag()

        self.assertEqual(repr(b), 'bag.Bag()')
        b.add(1)
        self.assertEqual(repr(b), 'bag.Bag(1)')
        b.add(2)
        self.assertEqual(repr(b), 'bag.Bag(1, 2)')

        b.add(b)
        self.assertEqual(repr(b), 'bag.Bag(1, 2, ...)')


if __name__ == '__main__':
    unittest.main()
