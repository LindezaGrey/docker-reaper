# docker-reaper
Container that stops docker containers based on their label. Example usage:
If you want a container to be terminated, set a label to it which name is "DeathDate" with the format 2018-01-01 00:00:00

    docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /etc/localtime:/etc/localtime:ro --name docker-reaper --restart always docker-reaper