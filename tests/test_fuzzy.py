from fuzzycategory import FuzzyCategory
import math
import unittest

class FuzzyCategoryTest(unittest.TestCase) :

  def test_uncorpused(self) :
      fuzzy = FuzzyCategory('name', [{'name' : 'thomas',
                                      'occupation' : 'welder'},
                                     {'name' : 'judy',
                                      'occupation' : 'machinist'}])
      assert math.isnan(fuzzy('thomas', 'hank'))
