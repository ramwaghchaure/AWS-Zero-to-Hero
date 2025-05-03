import json

def lambda_handler(event, context):
    # TODO implement
    print("**************************")
    print(event)
    print("**************************")
    number1 = event['number1']
    number2 = event['number2']

    sum = number1 + number2
    sub = number2 - number1
    mul = number1 * number2
    div = number2 / number1
    return {
        'statusCode': 200,
        'body' : {
      "sum" : sum,
      "sub"  : sub
      }
    }

