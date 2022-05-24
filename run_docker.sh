# RUN THIS TO MAKE THE DOCKER CONTAINERS
sudo docker-compose build && docker-compose up -d

#if port 80 is used, usually it's cause of apache2
#sudo /etc/init.d/apache2 stop
#if port 5432 is used, usually it's because of postgres taking 5432
#sudo systemctl disable postgresql