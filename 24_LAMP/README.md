# how-to :: SET UP A DIGITALOCEAN DROPLET
---
## Overview
- Using DigitalOcean to create servers
- Install ubuntu 20.04.02 and apache2 
- first part of LAMP (Linux, Apache, Mysql (swap for sqlite), Python/~~Pearl/PHP~~)

### Estimated Time Cost: 1 hour 

### Prerequisites:

- Have a GitHub account and obtain a GitHub Student Developer Pack. 
- Know the type of droplet you will need beforehand to make provisioning one quicker and easier.

1. Log into DigitalOcean with your GitHub account. 
2. Create a droplet with these options in place (some of this information was from Lia's comment on Piazza):  
    - Ubuntu 20.04 (LTS) x64
    - Basic droplet (shared CPU plan) 
    - Regular Intel ($5 per month)
    - A datacenter in New York
    - Choose SSH keys for authentication and follow the instructions on the side for how to create and/or add one
    - We don't want to enable backups ($1 per month), our code will be stored on GitHub
    - It is conventional to name servers in all lowercase
3. Go through the steps for creating and adding a sudo user on this [page](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart) (can use the web console for this), which is also under "Resources."
    First, enter this command:
    ```
    # adduser <username>
    ```
    Then, answer the questions that are presented to you.
    Lastly, enter this command to add the user to the sudo group:
    ```
    # usermod -aG sudo <username>
    ```
4. Access your droplet 
    - If you want to access the droplet via a terminal, ssh as root to your ipv4 address and say yes for the fingerprint and you should be in.
        ```
        $ ssh root@<ipv4 address>
        ```
        You can then do this to access your droplet as your sudo user:  
        ```
        # su <username>
        ```
    - You can also ssh as your sudo user directly:
        ```
        $ ssh <username>@<ipv4 address>
        ```
5. Once you ssh as root, you can follow the steps for setting up a basic firewall found [here](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04) (go to Step 4).  
    Follow these steps:
    1. ``` 
        # ufw app list 
        ``` 
        You should see
        ```
        Available applications:
            OpenSSH
        ```
    2. ``` 
        # ufw allow OpenSSH 
        ```
    3. ```
        # ufw enable
        ```
        Then, type y and enter.
    4. ```
        # ufw status
        ```
        You should see: 
        ``` 
        Status: active  

        To                         Action      From  
        --                         ------      ----  
        OpenSSH                    ALLOW       Anywhere  
        OpenSSH (v6)               ALLOW       Anywhere (v6)  
        ```

6. Once you ssh as root you can also run this command to add your ssh key to your sudo account:
    ```
    ssh-copy-id <username>@<remote_host>
    ```

7. Once you ssh as root you can also shut off root access.   
    First,  
    ```
    $ sudo nano /etc/ssh/sshd_config 
    ```
    Change PermitRootLogin yes to PermitRootLogin no and save

    Then,  
    ```
    $ sudo service ssh restart 
    ```

8. Once you ssh as your sudo account, install Apache using instructions found [here](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04) (go to Step 1).
    - Follow these steps:  
        1. ```
            $ sudo apt update
            ```
        2. ```
            $ sudo apt install apache2
            ```
            Then, type Y and enter.
        3. ```
            $ sudo ufw app list
            ```
            You should see:  
            ```
            Available applications:  
                Apache  
                Apache Full  
                Apache Secure  
                OpenSSH  
            ```
        4. ```
            $ sudo ufw allow in "Apache"
            ```
        5. ```
            $ sudo ufw status
            ```
            You should see:  
            ```
            Status: active  

            To                         Action      From  
            --                         ------      ----
            OpenSSH                    ALLOW         Anywhere                                  
            Apache                     ALLOW       Anywhere                    
            OpenSSH (v6)               ALLOW       Anywhere (v6)                      
            Apache (v6)                ALLOW       Anywhere (v6)  
            ```
        6. Check with http://your_server_ip and make sure the default Ubuntu 20.04 Apache web page shows up.

__NOTE:__ Some people may experience ssh issues when trying to ssh into their sudo account.   
Here's a possible workaround:  
This is the [source](https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh).  

1. Access droplet with root

2. run this command 
```
$ sudo nano /etc/ssh/sshd_config
```

3. Change PasswordAuthentication from no to yes 

4. Exit Nano and reload SSH config 
```
$ sudo service sshd reload
```

5. Set up ssh key for account 
```
$ ssh-copy-id <username>@<droplet_ip_address>
```

6. Revert back to no for PasswordAuthentication (technically optional)  

__ANOTHER NOTE:__ Some people may experience ssh issues when trying to ssh into their root account and sudo account through the terminal.   
Here's a possible workaround:  
It's Solution 1 from [here](https://phoenixnap.com/kb/ssh-permission-denied-publickey) (from Alif on Piazza). 

1. Access droplet with web console

2. run this command 
```
$ sudo nano /etc/ssh/sshd_config
```

3. Change PasswordAuthentication from no to yes 

4. Make sure ChallengeResponseAuthentication is no. If not, change it.

5. Exit Nano and restart the SSH service 
```
$ sudo service ssh restart
```
You can now ssh into your root account, but if you don't have a password, you can reset your root password by going to your droplet on the DigitalOcean website and clicking on "Access" on the side. Click "Reset Root Password" at the bottom and use the password provided to you through email. You will be prompted to create a new password afterwards. Do this.  

5. Set up ssh key for account 
```
$ ssh-copy-id <username>@<droplet_ip_address>
```

6. Revert back to no for PasswordAuthentication (technically optional)

### Resources
* Mainly used DigitalOcean documentation.
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart
* https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/to-existing-droplet/
* https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://phoenixnap.com/kb/ssh-permission-denied-publickey
* https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner

---

Accurate as of (last update): 2022-01-16

#### Contributors: 
Andy Lin, pd2  
Qina Liu, pd2  
Roshani Shrestha, pd2  