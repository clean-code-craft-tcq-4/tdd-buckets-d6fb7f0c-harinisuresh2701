import unittest
import current_samples_analysis

class TypewiseTest(unittest.TestCase):
  sample_set = [4,5]
  def check_current_samples(self):
    count_in_range = current_samples_analysis.occurance_in_range(sample_set)
    self.assertTrue(count_in_range == 2)
