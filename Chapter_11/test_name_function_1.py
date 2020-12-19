# testing a function (a failing test)
'''
(1) E
======================================================================
(2) ERROR: test_1st_last_name (__main__.NamesTestCase)
----------------------------------------------------------------------
(3) Traceback (most recent call last):
  File "d:\VS Code Programs\PythonCrashCourse2ndEd\Chapter_11\test_name_function_1.py", line 7, in test_1st_last_name
    self.assertEqual(get_formatted_name('maynard', 'keenan'), 'Maynard Keenan')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
(4) Ran 1 test in 0.001s

(5) FAILED (errors=1)
'''

'''
- get_formatted_name() in name_function_1.py is written to handle middle names

- That'll break the function for names with just 1st & last name, like Maynard Keenan

- The 1st item in the output is a single E (1), which tells us 1 unit test in the test case resulted in an error 

- Next, we see that test_1st_last_name() in NamesTestCase caused an error (2) 

- Knowing which test failed is critical when your test case contains many unit tests 

- At (3) we see a standard traceback, which reports that the function call get_formatted_name('maynard', 'keenan') 
  no longer works because it’s missing a required positional argument

- We also see that 1 unit test was run (4) 

- Finally, we see an additional message that the overall test case failed and that 1 error occurred when running the test case (5) 

- This information appears at the end of the output so you see it right away; 
  you don’t need to scroll up through a long output listing to find out how many tests failed
'''

import unittest
from name_function_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_1st_last_name(self):
        self.assertEqual(get_formatted_name('maynard', 'keenan'), 'Maynard Keenan')

if __name__ == '__main__':
    unittest.main()