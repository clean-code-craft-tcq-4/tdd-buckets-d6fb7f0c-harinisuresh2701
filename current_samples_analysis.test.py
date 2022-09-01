import unittest
import current_samples_analysis
import current_sensing

class TypewiseTest(unittest.TestCase):
  sample_set = [3, 3, 5, 4, 10, 11, 12]
  def check_find_range_count(self,sample_set):
    self.assertTrue(current_samples_analysis.find_range_count(sample_set)=={(10, 12, 3), (3, 5, 4)})
  
  def check_csv_formatter(self):
    self.assertTrue(current_samples_analysis.print_in_csv_format([3,5,7])=="3-5, 7")

  def check_error_handling(self):
    self.assertTrue(current_sensing.error_handling(4095)=="Current sample is out of valid range of [0 - 4094]!")
    self.assertTrue(current_sensing.error_handling(4093)=="All is well!")
    self.assertTrue(current_sensing.error_handling(40.3)=="Current sample is not a positive integer!")
    self.assertTrue(current_sensing.error_handling(-5)=="Current sample is not a positive integer!")
    self.assertTrue(current_sensing.error_handling(0)=="Warning : No current at all!")
    
  def check_sample_to_amp_conversion(self):
    self.assertTrue(current_sensing.sample_to_amp_conversion(0)==0)
    self.assertTrue(current_sensing.sample_to_amp_conversion(1146)==3)
    
