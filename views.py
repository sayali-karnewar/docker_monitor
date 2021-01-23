import aiohttp_jinja2
#from setup import setup_docker
import docker

@aiohttp_jinja2.template("get.html")
async def get(request):
    return {"status":"success"}

@aiohttp_jinja2.template("layout.html")
async def monitor(request):
    db = request.app['db']
    container_name = []
    container_started_at = []
    container_status = []
    container_ram = []
    container_cpu_percent = []
    try:
        client = docker.from_env()
        container_list = client.containers.list(all=True)
    except:
        print(1)    
    try:    
        for i in container_list:
            st = str(i)[12:-1]
            container = client.containers.get(st)
            container_name.append(container.attrs['Name'])
            container_started_at.append(container.attrs['State']['StartedAt'])
            container_status.append(container.attrs['State']['Status'])
            container_ram.append(container.attrs['HostConfig']['Memory'])
            container_cpu_percent.append(container.attrs['HostConfig']['CpuPercent'])
    except:
        print(2)
    n = len(container_name)

    container_list = []
    try:
        for i in range(n): 
            dic1 = {}
            dic1['container_name'] = container_name[i]
            dic1['started_at'] = container_started_at[i]
            dic1['status'] = container_status[i]
            dic1['ram'] = container_ram[i]
            dic1['cpu'] = container_cpu_percent[i]
            container_list.append(dic1)
    except:
        print(3)
    try:
        await db.collection.insert_many([[
                                {'container_name':container_name[i]}, 
                                {'container_started_at':container_started_at[i]},
                                {'container_status':container_status[i]}, 
                                {'container_ram':container_ram[i]}, 
                                {'container_cpu_percent':container_cpu_percent[i]}] for i in range(n)])    
    except:
        print(4)

    return {'container_list': container_list}