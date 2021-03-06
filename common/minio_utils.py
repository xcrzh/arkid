# pylint: disable=missing-docstring
import functools
from datetime import timedelta

from minio import Minio
from minio.error import (
    NoSuchBucket,
    ResponseError,
)

from django.conf import settings

EXPIRES = timedelta(days=3)

CLIENT = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_SECURE,
    region=settings.MINIO_LOCATION)


def put_object(bucket_name, object_name, file_data, length=None):
    if not CLIENT.bucket_exists(bucket_name):
        make_bucket(bucket_name)
    return CLIENT.put_object(bucket_name, object_name, file_data, length)


def get_object(bucket_name, object_name, response_headers=None):
    return CLIENT.get_object(bucket_name, object_name, response_headers)


def presign_put(bucket_name, object_name):
    return CLIENT.presigned_put_object(bucket_name, object_name, EXPIRES)


def presign_get(bucket_name, object_name, response_headers=None):
    return CLIENT.presigned_get_object(bucket_name, object_name, EXPIRES, response_headers)


def make_bucket(bucket_name):
    return CLIENT.make_bucket(bucket_name, location=settings.MINIO_LOCATION)
