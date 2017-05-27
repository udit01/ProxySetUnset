#######################################

# for bash

p1 = '/etc/bash.bashrc'
with open(p1) as bash:
    # with open('a.bashrc', 'r') as bash:
    file_text = bash.readlines()

uncomm_http = 'export http_proxy="http://proxy22.iitd.ac.in:3128"\n'
comm_http = '#' + uncomm_http

if comm_http in file_text:
    pass
elif uncomm_http in file_text:
    file_text.remove(uncomm_http)
    file_text.append(comm_http)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)

uncomm_https = 'export https_proxy="https://proxy22.iitd.ac.in:3128"\n'
comm_https = '#' + uncomm_https

if comm_https in file_text:
    pass
elif uncomm_https in file_text:
    file_text.remove(uncomm_https)
    file_text.append(comm_https)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)


##########################################################

# for apt

p1 = '/etc/apt/apt.conf'
with open(p1) as bash:
    # with open('a.bashrc', 'r') as bash:
    file_text = bash.readlines()

uncomm_http = 'Acquire::http { Proxy "http://proxy22.iitd.ac.in:3128"; }\n'
comm_http = '#' + uncomm_http

if comm_http in file_text:
    pass
elif uncomm_http in file_text:
    file_text.remove(uncomm_http)
    file_text.append(comm_http)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)

uncomm_http = 'Acquire::https { Proxy "https://proxy22.iitd.ac.in:3128"; }\n'
comm_https = '#' + uncomm_https

if comm_https in file_text:
    pass
elif uncomm_https in file_text:
    file_text.remove(uncomm_https)
    file_text.append(comm_https)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)



##########################################

#for apm

p1 = '/home/udit01/.atom/.apmrc'


with open(p1) as bash:
    # with open('a.bashrc', 'r') as bash:
    file_text = bash.readlines()

uncomm_http = 'http_proxy = "http://proxy22.iitd.ac.in:3128"\n'
comm_http = '#' + uncomm_http

if comm_http in file_text:
    pass
elif uncomm_http in file_text:
    file_text.remove(uncomm_http)
    file_text.append(comm_http)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)

uncomm_https = 'https_proxy = "https://proxy22.iitd.ac.in:3128"\n'
comm_https = '#' + uncomm_https

if comm_https in file_text:
    pass
elif uncomm_https in file_text:
    file_text.remove(uncomm_https)
    file_text.append(comm_https)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)

uncomm_proxy = 'proxy = "http://proxy22.iitd.ernet.in:3128/"\n'
comm_proxy = '#' + uncomm_https

if comm_proxy in file_text:
    pass
elif uncomm_proxy in file_text:
    file_text.remove(uncomm_proxy)
    file_text.append(comm_proxy)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)


#############################################

#for ZSH

p1 = '/etc/zsh/zshrc'
with open(p1) as bash:
    # with open('a.bashrc', 'r') as bash:
    file_text = bash.readlines()

uncomm_http = 'export http_proxy="http://proxy22.iitd.ac.in:3128"\n'
comm_http = '#' + uncomm_http

if comm_http in file_text:
    pass
elif uncomm_http in file_text:
    file_text.remove(uncomm_http)
    file_text.append(comm_http)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)

uncomm_https = 'export https_proxy="https://proxy22.iitd.ac.in:3128"\n'
comm_https = '#' + uncomm_https

if comm_https in file_text:
    pass
elif uncomm_https in file_text:
    file_text.remove(uncomm_https)
    file_text.append(comm_https)
else:
    pass

with open(p1, 'w') as bash:
    bash.writelines(file_text)


#####################################################

#for npm
