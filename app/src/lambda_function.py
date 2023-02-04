from .handlers import ec2_handler
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('f{event}, iniciando função EC2')

    ec2_handler.lambda_handler_ec2(event)
