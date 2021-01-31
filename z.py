import docker

client = docker.from_env()
client.containers.run("ubuntu")
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

    
n = len(container_list)

try:    
        for i in range(n):
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