market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    print(stoplight)
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    print(stoplight)
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight) 

switch_lights(market_2nd) 