# Copyright (c) Facebook, Inc. and its affiliates.
import time
import unittest

from mmf.utils.timer import Timer


class TestUtilsTimer(unittest.TestCase):
    def test_get_current(self):
        timer = Timer()
        expected = "0ms"

        self.assertEqual(timer.get_current(), expected)

    def test_reset(self):
        timer = Timer()
        time.sleep(2)
        timer.reset()
        expected = "0ms"

        self.assertEqual(timer.get_current(), expected)

    def test_get_time_since_start(self):
        timer = Timer()
        time.sleep(2)
        expected = "2s"

        self.assertTrue(expected in timer.get_time_since_start())
