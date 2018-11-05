import docker
from datetime import datetime
import time

client = docker.from_env()
print("Let the killing begin :]")
while True:
        # print("ein neuer zyklus beginnt")
        # check all containers on the host
        for container in client.containers.list():
                # print("scanning...found:", container.name)
                if 'DeathDate' in container.attrs['Config']['Labels']:
                        # get the deathdate label of the containers in order to shut them down
                        DeathDate = datetime.strptime(container.attrs['Config']['Labels']['DeathDate'], '%Y-%m-%d %H:%M:%S')
                        if datetime.now() > DeathDate:
                                container.stop()
                                container.remove()
                                print("stopped and removed:", container.name)
                                # also remove all persistent volumes
                                for mount in [client.volumes.get(volume['Name']) for volume in container.attrs['Mounts']]:
                                        mount.remove()
                                        print("removed volume:",mount)
        time.sleep(60)