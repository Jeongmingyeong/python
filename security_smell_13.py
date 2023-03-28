file_name = input()
exec(f'sudo mkdir {file_name}') # Exec Statement

os.chmod('/etc/hosts', Oo777) # Bad File Permission

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 31137)) # Hard-coded IP Address Binding

if username == 'root' and password == '123' : # Hard-coded Secret
    logIn()

username = 'root'
password = '' # Empty Password

initServer('127.0.0.1').simple_bind_s(username, password)
hardcoded_tmp_directory = \
    ['/tmp', '/var/tmp', '/dev/shm'] # Hard-coded tmp Directory

try: do_some_stuff()
except : pass # (or continue) # Ignore Except Block

app.run(debug=True) # Debug Set to True in Deployment

requests.get('https://gmail.com', verify=False) # No Certificate Validation

requests.get('http://www.apache.org') # Use of HTTP without TLS

service_name = input()
subprocess.Popen(f'sudo systemctl restart {service_name}'
                 , shell=True) # Command Injection

query = "DELETE FRO< foo WHERE id = '%s'" % user_input
result = connection.execute(query) # Constructing SQL upon Input

response = urllib.urlretrieve("192.168.1.1/example.iso"
                              , "example.iso") # No Integirty Check