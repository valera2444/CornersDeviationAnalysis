import unittest
from DrawingPlots import DrawPlots
import pandas as pd

class TestDrawMethods(unittest.TestCase):
    def setUp(self):
        self.drawer = DrawPlots()
        self.data = pd.read_json('deviation.json')

    def test_draw_pie(self):
        self.assertEqual(len(self.drawer._DrawPlots__draw_boxplot(self.data)), 2)

    def test_draw_heatmap(self):
        self.assertTrue('sns_heatmap' in self.drawer._DrawPlots__draw_heatmap(self.data)[0])

if __name__ == '__main__':
    unittest.main()