def devices(data): 
    if data['count'] > 0:
        output = f'**Devices**:\n'
        for obj in data['results']:
            dev_type = obj['device_type']['display']
            site = obj['site']['display']
            name = obj['name']
            url = obj['url'].replace('/api/', '/')
            output += f'\nName: {name}'
            output += f'\nURL: {url}'
            output += f'\nDevice Type: {dev_type}'
            output += f'\nSite: {site}'
            output += f'\n--------\n'
            
        output += '\n'
    else:
        output = ''
    
    return output
        
def ip(data):
    if data['count'] > 0:
        output = f'**IPs**:\n'
        for obj in data['results']:
            address = obj['address']
            output += f'\nAddress: {address}'
            url = obj['url'].replace('/api/', '/')
            output += f'\nURL: {url}'
            if obj['dns_name'] != '':
                dns_name = obj['dns_name']
                output += f'\DNS Name: {dns_name}'
            if obj['assigned_object_id'] is not None:
                parent_key_map = {
                    'virtualization.vminterface': 'virtual_machine',
                    'dcim.interface': 'device'
                }
                assigned_obj_name = obj['assigned_object']['display']
                object_key = parent_key_map[obj['assigned_object_type']]
                device = obj['assigned_object'][object_key]['display']
                assigned_obj_url = obj['assigned_object']['url'].replace('/api/', '/')
                output += f'\nAssigned: {device} - {assigned_obj_name}'
                output += f'\nAssigned URL: {assigned_obj_url}'
            output += f'\n--------\n'

        output += '\n'
    else:
        output = ''
    
    return output

def aggregates(data):
    if data['count'] > 0:
        output = f'**Aggregates**:\n'
        for obj in data['results']:
            prefix = obj['prefix']
            output += f'\nPrefix: {prefix}'
            url = obj['url'].replace('/api/', '/')
            output += f'\nURL: {url}'
            if obj['description'] != '':
                description = obj['description']
                output += f'\nDescription: {description}'
            output += f'\n--------\n'
        output += '\n'
    else:
        output = ''

    return output

def prefixes(data):
    if data['count'] > 0:
        output = f'**Prefixes**:\n'
        for obj in data['results']:
            prefix = obj['prefix']
            output += f'\nPrefix: {prefix}'
            url = obj['url'].replace('/api/', '/')
            output += f'\nURL: {url}'
            if obj['description'] != '':
                description = obj['description']
                output += f'\nDescription: {description}'
            output += f'\n--------\n'
        output += '\n'
    else:
        output = ''

    return output

def sites(data):
    if data['count'] > 0:
        output = f'**Sites**:\n'
        for obj in data['results']:
            name = obj['name']
            url = obj['url'].replace('/api/', '/')
            output += f'\nName: {name}'
            output += f'\nURL: {url}'
            if obj['region'] is not None:
                if 'display' in obj['region']:
                    region = obj['region']['display']
                    output += f'\nRegion: {region}'
            output += f'\n--------\n'
        output += '\n'
    else:
        output = ''

    return output