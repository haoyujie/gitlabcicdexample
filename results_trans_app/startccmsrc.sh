#source ./ccmpy3_venv/bin/activate
#python3 ./src/ccmatsrv.py & 
cd $(dirname $0)
python3 ./src/ccmatserver.py | tee ccmatser.log

