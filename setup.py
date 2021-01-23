import motor.motor_asyncio
import docker

async def setup():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.docker_monitor
    return db


async def setup_docker():
    client = docker.from_env()
    container_list = client.containers.list(all=True)
    for i in container_list:
        st = str(i)[12:-1]
        container = client.containers.get(st)
    print(st, container.attrs['Name'] ,container.attrs['State']['StartedAt'] ,container.attrs['State']['Status'])
    
    return container_list