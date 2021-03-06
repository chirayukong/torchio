#!/usr/bin/env python

"""Tests for `torchio` package."""


import unittest
import numpy as np
from numpy.testing import assert_raises, assert_array_equal
import torchio
from torchio import INTENSITY, LABEL


class TestRandomElasticDeformation(unittest.TestCase):
    """Tests for `RandomElasticDeformation`."""

    def setUp(self):
        """Set up test fixtures, if any."""
        shape = 1, 10, 20, 30
        np.random.seed(42)
        affine = np.diag((1, 2, 3, 1))
        affine[:3, 3] = 40, 50, 60
        self.sample = {
            't1': dict(
                data=self.getRandomData(shape),
                affine=affine,
                type=INTENSITY,
            ),
            't2': dict(
                data=self.getRandomData(shape),
                affine=affine,
                type=INTENSITY,
            ),
            'label': dict(
                data=(self.getRandomData(shape) > 0.5).astype(np.float32),
                affine=affine,
                type=LABEL,
            ),
        }

    @staticmethod
    def getRandomData(shape):
        return np.random.rand(*shape)

    def test_random_elastic_deformation(self):
        transform = torchio.transforms.RandomElasticDeformation(
            proportion_to_augment=1,
            seed=42,
        )
        keys = ('t1', 't2', 'label')
        fixtures = 788.684351305757, 782.1046020679798, 851
        transformed = transform(self.sample)
        for key, fixture in zip(keys, fixtures):
            # # https://stackoverflow.com/a/38507093/3956024
            # assert_raises(
            #     AssertionError,
            #     assert_array_equal,
            #     self.sample[key]['data'],
            #     transformed[key]['data'],
            # )
            assert transformed[key]['data'].sum() == fixture
