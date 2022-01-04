def authorize(client, message):
    authorized_roles =  set(['BotUser'])
    authorized_servers = ['chatbot']
    authorized_channels = ['geral']

    author = message.author
    author_roles = set([ role.name for role in author.roles])
    
    if message.author == client.user:
        return False
    
    if str(message.guild) not in  authorized_servers:
        return False
    
    if str(message.channel) not in  authorized_channels:
        return False    

    if len( authorized_roles.intersection(author_roles) ) == 0:
        return False   

    return True

