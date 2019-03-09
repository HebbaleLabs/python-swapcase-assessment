import unittest
from swapcase import swapcharactercase
from parameterized import parameterized

class SwapCaseTest(unittest.TestCase):

  @parameterized.expand([
    ('short string with lowercase chars', 'abc', 'ABC'),
    ('short string with uppercase chars', 'XYZ', 'xyz'),
    ('short string with mixedcase chars', 'abcxyzABCXYZ', 'ABCXYZabcxyz')
  ])
  def test_swap_simple(self, name, input_value, expected):
    self.longMessage = True
    actual = swapcharactercase(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)

  @parameterized.expand([
    ('empty string', '', ''),
    ('string with spaces', 'The sky is clear', 'tHE SKY IS CLEAR'),
    ('string with other chars', 'Chicago P.D.', 'cHICAGO p.d.')
  ])
  def test_swap_specialchars(self, name, input_value, expected):
    self.longMessage = True
    actual = swapcharactercase(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)

  @parameterized.expand([
    ('long string with lowercase chars', 'pleasewaitoutsidethehouse', 'PLEASEWAITOUTSIDETHEHOUSE'),
    ('long string with uppercase chars', 'ROCKMUSICAPPROACHESATHIGHVELOCITY', 'rockmusicapproachesathighvelocity'),
    ('long string with mixedcase chars', 'EngInEErIngrEspOnsIbIlIty', 'eNGiNeeRiNGReSPoNSiBiLiTY'),
    ('long string with mixedcase chars and separators', 'It\'s Not All It\'s Cracked Up To Be', 'iT\'S nOT aLL iT\'S cRACKED uP tO bE'),
    ('long string with alphanum chars', 'I often see the time 11:11 or 12:34 on The Big Ben.', 'i OFTEN SEE THE TIME 11:11 OR 12:34 ON tHE bIG bEN.')
  ])
  def test_swap_perf(self, name, input_value, expected):
    self.longMessage = True
    actual = swapcharactercase(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)