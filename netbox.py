import aiohttp


async def get(endpoint, params = {}):
    api_token = "<netbox_api_key>"
    url = 'https://demo.netbox.dev/api'
    headers = {
        'accept': 'application/json',
        'Authorization': f"Token {api_token}",
    }
    URI = f"{url}{endpoint}"
    output = {}
    async with aiohttp.ClientSession() as session:
        async with session.get(URI, headers=headers, params=params, ssl=False) as resp:
            response =  await resp.json()
            output['count'] = response['count']
            output['results'] = []
            output['results'] = output['results'] + response['results']
        while response['next'] is not None:
            async with session.get(response['next'], headers=headers, params=params, ssl=False) as resp:
                response =  await resp.json()
                output['results'] = output['results'] + response['results']
        return output
