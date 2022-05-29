import base64
import six
import uuid
import imghdr
import io
import os
import environ
import boto3

env = environ.Env()
environ.Env.read_env()

AWS_ACCESS_KEY = env('AWS_ACCESS_KEY')
AWS_SECRET_KEY = env('AWS_SECRET_KEY')
AWS_REGION = env('AWS_REGION')
AWS_PASSWORD = env('AWS_PASSWORD')
BUCKET = env('BUCKET')


def get_file_extension(file_name, decoded_file, type):
    extension = imghdr.what(file_name, decoded_file)
    if type == 'video':
        extension = 'mp4'
    else:
        extension = "jpg" if extension == "jpeg" else extension
    return extension


def decode_base64_file(data, type):
    """
    Fuction to convert base 64 to readable IO bytes and auto-generate file name with extension
    :param data: base64 file input
    :return: tuple containing IO bytes file and filename
    """
    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file, type)

        complete_file_name = "%s.%s" % (file_name, file_extension,)

        return io.BytesIO(decoded_file), complete_file_name


def upload_base64_file(base64_file, type):
    bucket_name = BUCKET
    file, file_name = decode_base64_file(base64_file, type)
    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)

    client.upload_fileobj(
        file,
        bucket_name,
        file_name,
        ExtraArgs={'ACL': 'public-read'}
    )
    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"


