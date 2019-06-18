import asyncio
from aiohttp import web
from web.myjinja import html
from urllib.parse import parse_qs
from web.usercheck import checkuserinfo
import os

async def check(login):
    username = parse_qs(login.query_string)['username'][0]
    password = parse_qs(login.query_string)['password'][0]

    if checkuserinfo(username, password, filename=os.path.join(os.getcwd(), "userinfo.txt")):

        return web.Response(body=html('success.html'), content_type='text/html')
    else:
        with open('./templates/fail.html', encoding='utf-8') as f:
            data2 = f.read()
        return web.Response(body=data2, content_type='text/html')


async def index(request):

    with open('./templates/login.html', encoding='utf-8') as f:
        data = f.read()
    data1 = web.Response(body=data, content_type='text/html')

    return data1
async def success(request):
    with open('./templates/success.html', encoding='utf-8') as f:
        data = f.read()
    data1 = web.Response(body=data, content_type='text/html')

    return data1

async def fail(request):

    with open('./templates/fail.html', encoding='utf-8') as f:
        data = f.read()
    data2 = web.Response(body=data, content_type='text/html')

    return data2

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/check', check)

    app.router.add_route('GET', '/success', success)

    app.router.add_route('GET', '/fail', fail)
    runner = web.AppRunner(app)
    await runner.setup()
    print('http://localhost:10000')
    site = web.TCPSite(runner=runner, port=10000)
    await site.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()