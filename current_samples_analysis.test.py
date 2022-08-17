import unittest
import current_samples_analysis

class TypewiseTest(unittest.TestCase):
  sample_set = [3, 3, 5, 4, 10, 11, 12]
  def check_find_range_and_count(self,sample_set):
    self.assertTrue(current_samples_analysis.find_range_and_count(sample_set)=={(10, 12, 3), (3, 5, 4)})
  
  def check_print_in_csv_format(self):
    self.asserTrue(current_samples_analysis.print_in_csv_format([3,5,7])=="3-5, 7")
