import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Process SQS message.
    """
    for record in event['Records']:
        try:
            # Extract message body
            message_body = json.loads(record['body'])
            logger.info(f"Processing message: {message_body}")

            # Example: process the message (add your business logic here)
            result = process_message(message_body)
            logger.info(f"Message processed successfully: {result}")

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            raise e

def process_message(message):
    """
    Example processing function.
    """
    # Simulated processing logic
    return {"status": "success", "message": message}
