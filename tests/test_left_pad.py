import unittest

from publish_test import left_pad


class LeftPadTests(unittest.TestCase):

    def test_empty_iterable(self) -> None:
        self.assertEqual(left_pad('foo', 5), '  foo')
        self.assertEqual(left_pad('foobar', 6), 'foobar')
        self.assertEqual(left_pad('toolong', 2), 'toolong')
        self.assertEqual(left_pad(1, 2, '0'), '01')
        self.assertEqual(left_pad(17, 5, 0), '00017')


if __name__ == '__main__':
    unittest.main()
