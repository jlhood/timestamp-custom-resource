"""Lambda function handler."""

# must be the first import in files with lambda function handlers
import lambdainit  # noqa: F401

import datetime
import uuid

import cfn_resource

import lambdalogging

LOG = lambdalogging.getLogger(__name__)

# Lambda handler function
handler = cfn_resource.Resource()


@handler.create
def create(event, context):
    """Logic for resource create.

    Generate timestamp and return as response data.
    """
    LOG.debug('CustomResource create handler called with event: %s', event)
    physical_resource_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now().isoformat()
    return _response(physical_resource_id, timestamp)


@handler.update
def update(event, context):
    """Logic for resource create.

    Generate timestamp and return as response data.
    """
    LOG.debug('CustomResource update handler called with event: %s', event)
    physical_resource_id = event['PhysicalResourceId']
    timestamp = datetime.datetime.now().isoformat()
    return _response(physical_resource_id, timestamp)


@handler.delete
def delete(event, context):
    """Logic for resource delete.

    Clear subscription filter policy on resource delete.
    """
    LOG.debug('CustomResource delete handler called with event: %s', event)
    physical_resource_id = event['PhysicalResourceId']
    return _response(physical_resource_id, None)


def _response(physical_resource_id, timestamp):
    response = {
        "Status": "SUCCESS",
        "PhysicalResourceId": physical_resource_id,
        "Data": {
            "Timestamp": timestamp
        }
    }
    LOG.debug('Returning response: %s', response)
    return response
