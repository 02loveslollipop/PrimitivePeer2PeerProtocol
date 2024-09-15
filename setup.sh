#Build images
sudo docker build -t p4_peer:0.0.1 Peer/
sudo docker build -t p4_server:0.0.1 Server/
#running docker compose
sudo docker-compose -f docker-compose.yml up -d