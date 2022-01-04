import re

SUPPORTED_QUESTIONS = {}

def question_register(pattern, name="", description=""):
    
    def decorator(func):
        SUPPORTED_QUESTIONS[pattern] = {
            'name': name,
            'description': description,
            'function':   func
        }
        return func

    return decorator

@question_register(r'[Hh]elp', name="Help", description="Display bot functions")
async def help(**kwargs):
    output = ">>> "
    for pattern in SUPPORTED_QUESTIONS:
        name = SUPPORTED_QUESTIONS[pattern]['name']
        description = SUPPORTED_QUESTIONS[pattern]['description']
        output += f"Name: {name}\n"
        output += f"Description: {description}\n"
        output += f"Pattern: {pattern}\n\n"
    return output

async def process(content):
    
    for pattern in SUPPORTED_QUESTIONS:
        query_re = re.compile(pattern)
        match = query_re.match(content)
        if match:
            func = SUPPORTED_QUESTIONS[pattern]['function']
            kwargs = match.groupdict()
            output = await func(**kwargs)
            
            if output != '':
                return output          
    return None
