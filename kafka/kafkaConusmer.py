from kafka.consumer import KafkaConsumer
from kafka.producer import KafkaProducer
from json import loads

def kafkaconsumer():

    BOOTSTRAP_SERVER = 'localhost:9092'

    consumer = KafkaConsumer(
        'order.fulfillment',
        BOOTSTRAP_SERVER,
        auto_offset_reset = 'earliest',
        enable_auto_commit=False,
        group_id='test_groupid',
        value_deserializer=lambda x: loads(x.decode('utf-8'))

    )

    fulfillment_message = []
    for message in consumer:
        message = message.value_deserializer
        fulfillment_message.append(message)
    return fulfillment_message

def main():
    message_consumed = kafkaconsumer()
    for msg in message_consumed:
        print(f' message value {msg}')


if __name__ == '__main__':
    main()

