import boto3


def list_resources():
    cloudformation = boto3.resource('cloudformation')
    stack = cloudformation.Stack('TestStack')
    resources = []

    for r in stack.resource_summaries.all():
        resources.append(
            {'type': r.resource_type, 'physical_id': r.physical_resource_id, 'logical_id': r.logical_resource_id,
             'status': r.resource_status,
             'last_updated': r.last_updated_timestamp.isoformat()})

    sorted_list = sorted(resources, key=lambda x: (x['type'], x['last_updated']))

    for r in sorted_list:
        print(r)
