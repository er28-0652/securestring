# securestring

Windows SecureString wrapper written by Python.  
This script uses PowerShell as a backend, thus available only in Windows.  

## Install
```bash
$ pip install securestring
```

## Usage
```python
from securestring import securestring

plain_text = 'tesuya'

enc = securestring.encrypt(plain_text)

dec = securestring.decrypt(enc)
# tesuya
```