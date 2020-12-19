'''
- Python provides a number of assert methods in the unittest.TestCase class 

- As mentioned earlier, assert methods test whether a condition you believe is true at a specific point in your code is indeed true. 

- If the condition is true as expected, your assumption about how that part of your program behaves is confirmed; 
  you can be confident that no errors exist. 

- If the condition you assume is true is actually false, Python raises an exception

- With these methods you can verify that returned values equal or don’t equal expected values, 
  that values are True or False and that values are in or not in a given list.

- You can use these methods only in a class that inherits from unittest.TestCase,
  so let’s look at how we can use 1 of these methods in the context of testing an actual class.

Method                              Use
--------------------------------------------------------------------
assertEqual(a, b)                   Verify that a == b

assertNotEqual(a, b)                Verify that a != b

assertTrue(x)                       Verify that x is True

assertFalse(x)                      Verify that x is False

assertIn(item, list)                Verify that item is in list

assertNotIn(item, list)             Verify that item is not in list
'''

'''
- Testing a class is similar to testing a function — 
  much of your work involves testing the behavior of the methods in the class. 

- But there are a few differences, so let’s write a class to test. 

- Consider a class that helps administer anonymous surveys
'''
class AnonymousSurvey:
    """ Collect anonymous answers to a survey question """
    def __init__(self, question):
        """ store a question & prepare to store responses """
        self.question = question

        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        """ store a single response to the survey """
        self.responses.append(new_response)
    
    def show_results(self):
        print('\nSurvey results:')

        for response in self.responses:
            print(f'\n\t- {response}')

