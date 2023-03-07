import json

import boto3
from botocore.exceptions import ClientError

import constants


def pop_conversation(previous_conversation_response=None):
    return previous_conversation_response.pop(0)


def get_secret(secret_key):
    """

    :param secret_key:  secret key name
    :return:            decrypted secrets
    """
    secret_name = constants.secret_name
    region_name = constants.region_name

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = json.loads(get_secret_value_response['SecretString'])

    return secret[secret_key]
