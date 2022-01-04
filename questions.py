from dispacher import question_register
import netbox
import parsers
import asyncio
import time


@question_register(r'[Pp]ing', name="Ping", description="Says Pong")
async def ping():
    return "Pong"

@question_register(r'[Ss]leep (?P<query>\d+)', name="Sleep", description="Sleep for <query> times")
async def sleep(query):
    time.sleep(int(query))
    return f"slept for {query} seconds"

@question_register(r'[Aa]io[Ss]leep (?P<query>\d+)', name="Async Sleep", description="Async Sleep for <query> times")
async def aiosleep(query):
    await asyncio.sleep(int(query))
    return f"Async slept for {query} seconds"

@question_register(r'[Ss]earch (?P<query>.+)', name="Search Netbox models", description="Search for <query> object")
async def search_all(query):
    model_endpoint_dict = {
        'devices': '/dcim/devices/',
        'sites': '/dcim/sites/',
        'ip': '/ipam/ip-addresses/',
        'aggregates': '/ipam/aggregates/',
        'prefixes': '/ipam/prefixes/',
    }
    coros = [ get_output(model, model_endpoint_dict[model], query)
              for model in model_endpoint_dict ]

    results = await asyncio.gather(*coros)
    output = '>>> '
    for result in results:
        output += result
    return output

async def get_output(model, endpoint, query):
    try:
        data = await netbox.get(endpoint, params={'q' : query})
        func = getattr(parsers, model)        
        return func(data)
    except KeyError as e:
        print("Parser not implemented")
    except Exception as e:
        print(e)
    return ''