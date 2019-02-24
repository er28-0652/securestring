import subprocess

POWERSHELL = 'powershell -c "{0}"'
SECURESTRING_ENCRYPT_CMD = 'ConvertTo-SecureString "{0}" -AsPlainText -Force | ConvertFrom-SecureString'
SECURESTRING_DECRYPT_CMD = '$s = ConvertTo-SecureString -String \'{0}\'; [System.Runtime.InteropServices.marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))'

def encrypt(plain_text):
    ''' encrypt plain text by SecureString. '''
    
    cmd = POWERSHELL.format(SECURESTRING_ENCRYPT_CMD.format(plain_text))
    return _execute(cmd)

def decrypt(enc_text):
    ''' decrypt SecureString encrypted string text. '''

    cmd = POWERSHELL.format(SECURESTRING_DECRYPT_CMD.format(enc_text))
    return _execute(cmd)

def _execute(cmd):
    ''' run any command and get stdout result as utf-8 string. '''

    # execute command
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    
    # check status code is ok
    # if it's not, will raise RuntimeError exception
    if p.returncode != 0:
        raise RuntimeError('"{0}" run fails, err={1}'.format(cmd, stderr.decode('sjis')))
    
    # return stdout utf-8 string
    return stdout.decode('utf-8').replace('\r\n', '')