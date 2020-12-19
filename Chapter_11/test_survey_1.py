# the setUp() method
'''
- In test_survey_0.py we created a new instance of AnonymousSurvey in each test method and 
  we created new responses in each method. 

- The unittest.TestCase class has a setUp() method that allows you to create these objects once and 
  then use them in each of your test methods. 

- When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with 'test_' 

- Any objects created in the setUp() method are then available in each test method you write
'''
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''
    - The method setUp() does 2 things: it creates a survey instance & a list of responses 

    - Each of these is prefixed by 'self', so they can be used anywhere in the class. 

    - This makes the 2 test methods simpler because neither one has to make a survey instance or a response

    - When we run test_survey_1.py again, both tests still pass. 

    - These tests would be particularly useful when trying to expand AnonymousSurvey to handle multiple responses for each person. 

    - After modifying the code to accept multiple responses, you could run these tests and 
      make sure you haven’t affected the ability to store a single response or a series of individual responses.

    - When you’re testing your own classes, the setUp() method can make your test methods easier to write. 

    - You make 1 set of instances & attributes in setUp() & then use these instances in all your test methods. 

    - This is much easier than making a new set of instances & attributes in each test method
    '''
    def setUp(self):
        """ this method creates a survey instance & a set of responses that can be used in all test methods """
        self.my_survey = AnonymousSurvey('What is your native tongue?')

        self.responses = ['English', 'Japanese', 'Spanish']
    
    def test_store_1_response(self):
        """ this method verifies that the 1st response in self.responses, which is self.responses[0], can be stored correctly """
        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_3_responses(self):
        """ this method verifies that all 3 responses in self.responses can be stored correctly """
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
