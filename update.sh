#Stop docker compose
sudo docker-compose stop
#rebuild images
clear
sudo docker build -t p4_peer:0.0.1 Peer/
sudo docker build -t p4_server:0.0.1 Server/
#Execute again docker compose
clear
sudo docker-compose -f docker-compose.yml up -d