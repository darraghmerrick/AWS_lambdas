"""
Create a Lambda Function within the AWS Lambda Console

    Navigate to the Lambda portion of the AWS Console.
    Select Create your Lambda Function from scratch.
    Select Python3.6 as your runtime.
    Deploy your function after adding the sample code.

Create a Test Event and Manually Invoke the Function Using the Test Event

    Select the drop-down next to Test at the top of the Lambda console.
    From the drop-down, select Configure test events.
    Select the Hello World event template.
    Erase the code in there and copy and paste the provided JSON code, then select Create.
    Click on the Test button and verify your function succeeds.

Verify that CloudWatch has Captured Function Logs

    Navigate to the CloudWatch portion of the AWS Console.
    Select Logs from the selection on the left.
    Select the log group with your function name in it.
    Select the log stream within the log group.
    Verify the output is present and correct.
    """

import json

print('Loading your function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # print statements actually get printed to the logs.
    print("message --> " + event['message'])

    # Actually returning the value of the 'message' key.
    return event['message']

    # Raising an exception if something goes wrong...
    raise Exception('Something went wrong!')

""""
Use this as a test message in the aws lamdba console
{
  "message": "Congrats, you have successfully ran a Lambda function",
  "notmessage": "If this shows, something went wrong"
}
"""
