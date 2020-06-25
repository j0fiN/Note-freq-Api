# Note-freq-Api
A simple REST api  to  get the frequency of musical notes.

### To run
```commandline
git clone https://github.com/j0fiN/Note-freq-Api.git 
cd Note-freq-Api
pip install -r requirements.txt
python api.py
```

### To use
```python
import requests
response  = requests.request("GET", url="http://localhost:5000/api?note=g%234") # notice the utf-8 for '#'
result = eval(response.content)
print(result) # prints {"frequency":830.61, "note":"G#", "octave":4}
```
