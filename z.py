import docker

client = docker.from_env()
#client.containers.run("ubuntu")
k = client.containers.list(all=True)
for i in k:
    st = str(i)[12:-1]
    container = client.containers.get(st)

    print(st, container.attrs['HostConfig']['Memory'] ,container.attrs['State']['StartedAt'] ,container.attrs['State']['Status'])

print(container.attrs)

#State, StartedAt, Name


container_list = [{"a":1, "a1":1}, {"a":2, "a1":2}, {"a":3, "a1":3}]

for i in container_list:
    print(i['a'], i['a1'])

    