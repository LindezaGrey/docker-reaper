import docker
from datetime import datetime
import time

client = docker.from_env()

while True:
        # check all containers on the host
        for container in client.containers.list():
                if 'DeathDate' in container.attrs['Config']['Labels']:
                        # get the deathdate label of the containers in order to shut them down
                        DeathDate = datetime.strptime(container.attrs['Config']['Labels']['DeathDate'], '%Y-%m-%d %H:%M:%S')
                        if datetime.now() > DeathDate:
                                container.stop()
                                print("stopped:", container.name)
                                # also remove all persistent volumes
                                for mount in [client.volumes.get(volume['Name']) for volume in container.attrs['Mounts']]:
                                        mount.remove()
        time.sleep(60)