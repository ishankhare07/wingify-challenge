For API docs please refer to the [wiki](https://github.com/ishankhare07/wingify-challenge/wiki)

### Setting up locally
1. Clone the repo  
  ```
    git clone git@github.com:ishankhare07/wingify-challenge.git
  ```
2. Create and activate a python virtual environment  
  ```
    pyvenv venv; . venv/bin/activate
  ```
3. Install dependencies  
  ```
    pip install -r requirements.txt
  ```
4. Set up a secret key. Current secret key setup is done as following:  
```python
import os
import hashlib
hashlib.sha512(os.urandom(24).hexdigest())  # returns a hex string
```
> Note this key only needs to be generated once and set and environment variable. This has already been taken care of while deploying to heroku.

  Next run `app.py`
```bash
python app.py
```
