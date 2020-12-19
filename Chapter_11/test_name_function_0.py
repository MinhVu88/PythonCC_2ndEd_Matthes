'''
- The module unittest from the Python standard library provides tools for testing your code. 

- A unit test verifies that 1 specific aspect of a function’s behavior is correct. 

- A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, 
  within the full range of situations you expect it to handle. 

- A good test case considers all the possible kinds of input a function could receive and 
  includes tests to represent each of these situations. 

- A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function. 

- Achieving full coverage on a large project can be daunting. 

- It’s often good enough to write tests for your code’s critical behaviors and 
  then aim for full coverage only if the project starts to see widespread use
'''

# testing a function (a passing test)
'''
- To write a test case for a function, import the unittest module & the function you want to test. 

- Then create a class that inherits from unittest.TestCase & write a series of methods to test different aspects of your function’s behavior.

- Here’s a test case with 1 method that verifies that the get_formatted_name() function works correctly when given a 1st & last name

- We call this method test_1st_last_name() as we’re verifying that names with only a 1st & last name are formatted correctly.

- Any method that starts with 'test_' will be run automatically when we run test_name_function.py. 

- Within this test method, we call the function we want to test. 

- In this example we call get_formatted_name() with the arguments 'adam' & 'jones' & place it inside an assert method
'''
import unittest
from name_function_0 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function_0.py' """
    def test_1st_last_name(self):
        """ Do names like 'Adam Jones' work? """
        '''
        - Assert methods verify that a result you received matches the result you expected to receive. 
        
        - In this case, because we know get_formatted_name() is supposed to return a capitalized, properly spaced full name, 
          we expect the value of formatted_name to be Adam Jones. 

        - To check if this is true, we use unittest’s assertEqual() method & pass it get_formatted_name('adam', 'jones') & 'Adam Jones'. 
        
        - self.assertEqual(get_formatted_name('adam', 'jones'), 'Adam Jones') says: 
                + Compare the value returned from get_formatted_name('adam', 'jones') to the string 'Adam Jones'. 
                + If they are equal as expected, fine. 
                + But if they don’t match, let me know!
        '''
        self.assertEqual(get_formatted_name('adam', 'jones'), 'Adam Jones')

'''
- We’re going to run this file directly but it’s important to note that 
  many testing frameworks import your test files before running them. 

- When a file is imported, the interpreter executes the file as it’s being imported 

- The if block below looks at a special variable, __name__, which is set when the program is executed 

- If this file is being run as the main program, the value of __name__ is set to '__main__' 

- In this case, we call unittest.main(), which runs the test case

- When a testing framework imports this file, the value of __name__ won’t be '__main__' & this block will not be executed

- When we run test_name_function.py, we get the following output:
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.000s
        OK

- The dot on the 1st line of output tells us that a single test passed. 

- The next line tells us that Python ran 1 test & it took less than 0.001 seconds to run. 

- The final OK tells us that all unit tests in the test case passed.

- This output indicates that get_formatted_name() will always work for names that 
  have a 1st & last name unless we modify the function. 

- When we modify get_formatted_name(), we can run this test again. 

- If the test case passes, we know the function will still work for names like Adam Jones
'''
if __name__ == '__main__':
    unittest.main()
