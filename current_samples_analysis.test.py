import unittest
import current_samples_analysis

class TypewiseTest(unittest.TestCase):
  sample_set = [3, 3, 5, 4, 10, 11, 12]
  def check_find_range_and_count(self,sample_set):
    self.assertTrue(current_samples_analysis.find_range_and_count(sample_set)=={(10, 12, 3), (3, 5, 4)})
  
  def check_current_samples(self):
    count_in_range = current_samples_analysis.occurance_in_range(sample_set)
    self.assertTrue(count_in_range == 2)
