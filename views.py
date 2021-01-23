import aiohttp_jinja2
#from setup import setup_docker
import docker

@aiohttp_jinja2.template("get.html")
async def get(request):
    return {"status":"success"}

@aiohttp_jinja2.template("layout.html.html")
async def monitor(request):
    db = request.app['db']
    container_name = []
    container_started_at = []
    container_status = []
    #container_cpu = []

    client = docker.from_env()
    container_list = client.containers.list(all=True)
    for i in container_list:
        st = str(i)[12:-1]
        container = client.containers.get(st)
        container_name.append(container.attrs['Name'])
        container_started_at.append(container.attrs['State']['StartedAt'])
        container_status.append(container.attrs['State']['Status'])

    n = len(container_name)

    container_list = []
    for i in range(n): 
        dic1 = {}
        dic1['container_name'] = container_name[i]
        container_list.append(dic1)
    
    await db.collection.insert_many([
                            {'container_name':container_name[i]}, 
                            {'container_started_at':container_started_at[i]},
                            {'container_status':container_status[i]}] for i in range(n))    

    
    return {'container_list': container_list}