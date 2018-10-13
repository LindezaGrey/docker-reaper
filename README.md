# docker-reaper
Container that stops docker containers based on their label. Example usage:

    docker run -d -v /var/run/docker.sock:/var/run/docker.sock --name docker-reaper docker-reaper