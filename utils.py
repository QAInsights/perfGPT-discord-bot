import json
import logging

import boto3
from botocore.exceptions import ClientError

import constants


def pop_conversation(previous_conversation_response=None):
    return previous_conversation_response.pop(0)


def get_secret(secret_key):
    """
    Read secrets from AWS
    :param secret_key:  secret key name
    :return:            decrypted secrets
    """
    secret_name = constants.SECRET_NAME
    region_name = constants.region_name

    # Create a Secrets Manager client

    try:

        if constants.profile_name is not None:
            session = boto3.session.Session(profile_name=constants.profile_name)
        else:
            # Take default AWS credentials from `~/.aws/credentials`
            session = boto3.session.Session()

    except ClientError as e:
        logging.info(e)
        exit(1)

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
        logging.info(e)
        exit(1)

    secret = json.loads(get_secret_value_response['SecretString'])

    return secret[secret_key]
