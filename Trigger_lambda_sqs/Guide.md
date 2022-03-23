Triggering AWS Lambda from Amazon SQS
Introduction

In this hands-on AWS lab, you will learn how to trigger a Lambda function using SQS. This Lambda function will process messages from the SQS queue and insert the message data as records into a DynamoDB table.
Solution

Log in to the AWS Management Console using the credentials provided on the lab instructions page. Make sure you're using the us-east-1 (N. Virginia) region.
Create the Lambda Function

    In the search bar on top, enter "lambda".
    From the search results, select Lambda.
    Click the Create function button.
    On the Create function page, select Author from scratch.
    Under Basic Information, set the following parameters for each field:

    Function name: Enter "SQSDynamoDB".
    Runtime: Select Python 3.8 from the dropdown menu.
    Execution role: Select Use an existing role.
    Existing role: Select lambda-execution-role from the dropdown menu,

    Click the Create function button.

Create the SQS Trigger

    Click the + Add trigger button.
    Under Trigger configuration, enter "sqs" in the search bar.
    From the search results, select Simple Queue Service.
    Under SQS queue, click the search bar and select Messages.
    Click Add.

Copy the Source Code into the Lambda Function

    Under the + Add trigger button, click the Code tab.
    On the left side, double-click on lambda_function.py.
    Delete the contents of the function.
    In a new browser tab or window, open up this link to the source code for lambda_function.py.
    Copy the code.
    Return to the AWS console and paste the code into the lambda_function.py code box.
    Click the Deploy button.

Log In to the EC2 Instance and Test the Script

    In the search bar on top of the console, enter "sqs".
    From the search results, select Simple Queue Service.
    Click Messages.
    Click the Monitoring tab to monitor our SQS messages.
    In the search bar on top, enter "ec2".
    From the search results, select EC2 and open it in a new browser tab or window.
    Under Resources, click Instances (running).
    In the existing instance available, click the checkbox next to its name.
    Click the Connect button at the top.
    Click Connect at the bottom to open a shell and access the command line.

    In the shell, become the cloud_user role:

    su - cloud_user

    View a list of files available to you:

    ls

    View the contents of the send_message.py file:

    cat send_message.py

    Start sending messages to our DynamoDB table from our Messages SQS queue with an interval of 0.1 seconds:

    ./send_message.py -q Messages -i 0.1

    After a few seconds, hit Control + C to stop the command from continuing to run.

Confirm Messages Were Inserted into the DynamoDB Table

    Return to the browser tab or window with the AWS console.
    In the search bar on top, enter "dynamodb".
    From the search results, select DynamoDB.
    In the left-hand navigation menu, select Tables.
    Select the Message table.

    In the top-right corner of the page, click Explore table itemsand review the list of items that were inserted from our script, sent to SQS, triggered Lambda, and inserted into the DynamoDB database.