import boto3
import logging
from constants import error_constants, status_code

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler_ec2(event, context):
    logger.info('f{event}, iniciando a chamada no handler EC2')

    try:
        regiao = event['headers'].get('us-east-1')
        ec2 = boto3.client('ec2', region_name=regiao)
        instancias = ec2.describe_instance_status(IncludeAllInstances=True)
        logger.info(f'{len(instancias)} instâncias em execução encontradas')

        return {
            'statusCode': status_code.OK,
            'body': instancias
        }

    except KeyError as e:
        logger.error('Região não fornecida no cabeçalho')

        return {
            'statusCode': status_code.BAD_REQUEST,
            'body': error_constants.error_chamada_ecs + e
        }

    # Middleware
    except Exception as e:
        return {
            'statusCode': status_code.INTERNAL_SERVER_ERROR,
            'body': str(e)
        }
