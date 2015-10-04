import uuid
import time
import boto
import json
from boto.sqs.message import RawMessage

AWSKey = ""
AWSSecret=""
queue = "pi-queue"

def addMessageToQueue(message):
    data = {
        'submitdate': time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
        'key': str(uuid.uuid1()),
        'message': str(message)
    }

    sqs = boto.connect_sqs(AWSKey, AWSSecret)
    q = sqs.create_queue(queue)

    m = RawMessage()
    m.set_body(json.dumps(data))
    status = q.write(m)

def readMessageFromQueue():
    sqs = boto.connect_sqs(AWSKey, AWSSecret)
    q = sqs.create_queue(queue)
    q.set_message_class(RawMessage)

    results = q.get_messages()
    ret = "Got %s result(s).\n\n" % len(results)

    for result in results:
        msg = json.loads(result.get_body())
        ret += "Message: %s\n" % msg['message']

    ret += "\n...done."
    return ret

message = "this is just a test"
addMessageToQueue(message)
print(readMessageFromQueue)
