import unittest
import logging

from darts.dataprocessing.transformers import BaseDataTransformer
from darts.utils.timeseries_generation import constant_timeseries
from darts import TimeSeries


class BaseDataTransformerTestCase(unittest.TestCase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    class DataTransformerMock(BaseDataTransformer):
        def __init__(self):
            def mock_ts_transform(series: TimeSeries, *args, **kwargs) -> TimeSeries:
                return series + 10

            super().__init__(ts_transform=mock_ts_transform,
                             name="DataTransformerMock")
            self.transform_called = False

        @staticmethod
        def ts_transform(series: TimeSeries) -> TimeSeries:
            return series + 10

    def test_input_transformed(self):
        # given
        test_input = constant_timeseries(value=1)
        mock = self.DataTransformerMock()

        # when
        transformed = mock.transform(test_input)

        expected = constant_timeseries(value=11)
        self.assertEqual(transformed, expected)