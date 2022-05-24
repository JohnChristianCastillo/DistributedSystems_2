docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
# remove all images
docker system prune -a