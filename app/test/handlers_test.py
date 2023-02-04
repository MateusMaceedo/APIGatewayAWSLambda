import unittest
from ..src.handlers import ec2_handler


class handlers_test(unittest.TestCase):
    def test_lambda_handler_with_valid_region(self):
        event = {
            'headers': {
                'region': 'us-west-2'
            }
        }
        response = ec2_handler.lambda_handler_ec2(event, None)
        self.assertEqual(response['statusCode'], 200)

    def test_lambda_handler_with_invalid_region(self):
        event = {
            'headers': {
                'region': 'invalid-region'
            }
        }
        response = ec2_handler.lambda_handler_ec2(event, None)
        self.assertEqual(response['statusCode'], 500)

    def test_lambda_handler_without_region(self):
        event = {}
        response = ec2_handler.lambda_handler_ec2(event, None)
        self.assertEqual(response['statusCode'], 500)


if __name__ == '__init__':
    unittest.main()
