import re

names_regex = re.compile(r'Agent \w+')

print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agent_names_regex = re.compile(r'Agent (\w)\w*')
print(agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

