import json

import json
import math
import itertools

def lambda_handler(event, context):
    # Check if there are query string parameters
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None :
        # Return welcome message in an HTTP response
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain"
            },
            "body": "Welcome to class evaluation sys"
        }
    else:
        # Get the query string parameters
        query_params = event.get('queryStringParameters', {})
    
        # Get the list of numbers from the query string parameter 'nums'
        nums_str = query_params.get('name', '')
        
        if nums_str == 'ids721':
            response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/plain"
                },
                "body": "This is the best class in Duke taught by Noah"
                }
        else:
            response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/plain"
                },
                "body": "This is a great class"
                }
    return response                
                    
