# respoding to a failed test
'''
- when a test fails, don’t change the test. 

- Instead, fix the code that caused the test to fail.

- Examine the changes you just made to the function & figure out how those changes broke the desired behavior
'''
import unittest
from name_function_2 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''
    - In this case get_formatted_name() used to require only 2 parameters: a 1st name & a last name. 

    - Now it requires a 1st name, middle name & last name. 

    - The addition of that mandatory middle name parameter broke the desired behavior of get_formatted_name(). 

    - The best option here is to make the middle name optional & then run the test case again. 

    - If it passes, we’ll move on to making sure the function handles middle names properly.

    - If a middle name is passed to the function, the full name will contain a 1st, middle & last name. 

    - Otherwise, the full name will consist of just a 1st & last name. 

    - Now the function should work for both kinds of names
    '''
    def test_1st_last_name(self):
        self.assertEqual(get_formatted_name('justin', 'chancellor'), 'Justin Chancellor')

    # adding a new test
    '''
    - Now that we know get_formatted_name() works for simple names again (1st name & last name), 
      let’s write a 2nd test for people who include a middle name. 

    - We do this by adding another method to the class NamesTestCase

    - We name this new method test_1st_last_middle_name(). 

    - The method name must start with test_ so the method runs automatically when we run test_name_function_2.py. 

    - We name the method to make it clear which behavior of get_formatted_name() we’re testing. 

    - As a result, if the test fails, we know right away what kinds of names are affected

    - They need to be descriptive so you can make sense of the output when your tests fail and 
      because Python calls them automatically, you’ll never have to write code that calls these methods
    '''
    def test_1st_last_middle_name(self):
        self.assertEqual(get_formatted_name('daniel', 'carey', 'edwin'), 'Daniel Edwin Carey')

if __name__ == '__main__':
    unittest.main()
