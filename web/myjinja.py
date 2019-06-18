from jinja2 import Environment, FileSystemLoader
def html(htmlfile):
    with open('userinfo.txt', 'r', encoding='utf-8') as f:
        tabels = f.readlines()
    env = Environment(loader=FileSystemLoader('./templates/'))
    tmeplate = env.get_template(htmlfile)

    return tmeplate.render(**locals())

