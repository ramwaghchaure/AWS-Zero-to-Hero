import json

cold_start_time = None
def lambda_handler(event, context):
    global cold_start_time

    if cold_start_time is None:
        time.sleep(3)
        cold_start_time = time.time()
        start_type = "cold start"
    else:
        start_type = "hot start"

        current_time = time.time()
        response = {
              "current_time"    :   current_time,
              "start_type"      :   start_type,
              "cold_start_time" :   cold_start_time
}
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

