import json

def main(event, context);
print("=====================")
print(event)
print("=====================")
print(context)
print("=====================")
return {
       'statusCode': 200,
       'body' : json.dumps('Hello from lambda')
}