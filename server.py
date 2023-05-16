import json
with open ('data.json','r',encoding='utf-8') as f:
    data=json.load(f)


def handler(event, context):
    body    = json.loads(event['body'])
    chat_id = body['message']['chat']['id']
    message = body['message']['text']


    if "/start" in message:
        data3 = ''

        for i in range(len(data)):
            data2 = ''
            for key,value in data[i].items():
                data2 = data2 + f'{key} : {value} , '
            data3 = data3 + '\n\n' + data2
        text=data3

    elif '/help' in message:
        text = '/start - контактные данные мясокомбинатов'

    else:
        text    = message

    r = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(
                {
                    'parse_mode': 'HTML',
                    'method'    : 'sendMessage',
                    'chat_id'   : chat_id,
                    'text'      : text
                }
            ),
            'isBase64Encoded': False
        }

    return r
