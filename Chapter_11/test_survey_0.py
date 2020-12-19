# testing the AnonymousSurvey class in survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_1_response(self):
        """ check whether a single response is stored properly """
        my_survey = AnonymousSurvey('What is your native tongue?')

        my_survey.store_response('German')

        self.assertIn('German', my_survey.responses)
    
    # a survey is useful only if it generates more than 1 response
    def test_store_3_responses(self):
        """ check whether 3 responses are stored properly """
        my_survey = AnonymousSurvey('What other languages can you speak?')

        responses = ['English', 'Japanes', 'Spanish']

        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()