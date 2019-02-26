import unittest
from delayed_assert import expect, assert_expectations
from swapcase import swapcharactercase

class SwapCaseTest(unittest.TestCase):

  def test_swap_lowercase(self):
    expect( lambda: self.assertEqual(swapcharactercase('abc'), 'ABC'))
    assert_expectations()

  def test_swap_uppercase(self):
    expect( lambda: self.assertEqual(swapcharactercase('XYZ'), 'xyz'))
    assert_expectations()

  def test_swap_emptystring(self):
    expect( lambda: self.assertEqual(swapcharactercase(''), ''))
    assert_expectations()

  def test_swap_mixedcase(self):
    expect( lambda: self.assertEqual(swapcharactercase('abcxyzABCXYZ'), 'ABCXYZabcxyz'))
    assert_expectations()

  def test_swap_mixedcase_separated_by_space(self):
    expect( lambda: self.assertEqual(swapcharactercase('The sky is clear'), 'tHE SKY IS CLEAR'))
    assert_expectations()

  def test_swap_mixedcase_separated_by_otherchars(self):
    expect( lambda: self.assertEqual(swapcharactercase('Chicago P.D.'), 'cHICAGO p.d.'))
    assert_expectations()

  def test_swap_lowercase_longstring(self):
    expect( lambda: self.assertEqual(swapcharactercase('pleasewaitoutsidethehouse'), 'PLEASEWAITOUTSIDETHEHOUSE'))
    assert_expectations()

  def test_swap_uppercase_longstring(self):
    expect( lambda: self.assertEqual(swapcharactercase('ROCKMUSICAPPROACHESATHIGHVELOCITY'), 'rockmusicapproachesathighvelocity'))
    assert_expectations()

  def test_swap_mixedcase_longstring(self):
    expect( lambda: self.assertEqual(swapcharactercase('EngInEErIngrEspOnsIbIlIty'), 'eNGiNeeRiNGReSPoNSiBiLiTY'))
    assert_expectations()

  def test_swap_mixedcase_with_seperators_longstring(self):
    expect( lambda: self.assertEqual(swapcharactercase('It\'s Not All It\'s Cracked Up To Be'), 'iT\'S nOT aLL iT\'S cRACKED uP tO bE'))
    assert_expectations()

  def test_swap_alphanum(self):
    expect( lambda: self.assertEqual(swapcharactercase('I often see the time 11:11 or 12:34 on The Big Ben.'), 'i OFTEN SEE THE TIME 11:11 OR 12:34 ON tHE bIG bEN.'))
    assert_expectations()