#Start Flask /Server/server.py in the background and run the tests in test/test.py
# This script is used to start the server and run the tests
echo "Activating conda environment"
# init conda and activate the environment p2p
source ~/anaconda3/etc/profile.d/conda.sh
conda activate p2p

echo "Starting Flask server"
python ../Server/server.py &
echo "Waiting for server to start"
sleep 1
echo "Running tests in test/test.py"
python server.py