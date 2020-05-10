import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.StrictRedis(host='queue', port=6379, db=0)
    print('Aguardando mensagens...')
    while True:
        data = r.blpop('sender')[1]
        mensagem = json.loads(data)
        print('Enviando mensagem:', mensagem['assunto'])
        sleep(randint(15,45))
        print('Mensagem: ', mensagem['assunto'], ' enviada com sucesso')