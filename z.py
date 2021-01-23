import docker

client = docker.from_env()
#client.containers.run("ubuntu")
k = client.containers.list(all=True)
for i in k:
    st = str(i)[12:-1]
    container = client.containers.get(st)

    #print(st, container.attrs['Name'] ,container.attrs['State']['StartedAt'] ,container.attrs['State']['Status'])

print(container.attrs)

#State, StartedAt, Name