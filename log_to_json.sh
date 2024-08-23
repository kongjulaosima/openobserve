export TZ='Asia/Shanghai'
cd /home/lenovo/OpenObserve
python3 log_to_json.py
curl http://localhost:5080/api/default/default/_json -i -u "root@example.com:Complexpass#123"  -d "@logs.json"