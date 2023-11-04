To create virtual enviroment    
    py -3 -m venv venv

script for command terminal line to attach to virtuall enviroment
    venv\Scripts\activate.bat

check installed dependancies
    pip freeze

To Start web server
    uvicorn app.main:app --reload


webserver
    http://127.0.0.1:8000



install sql Alchemy
    pip install sqlalchemy
        2.0 is current version

Install fastapi
    pip install fastapi[all]



Install password hash algorith with bcrypt
    pip install "passlib[bcrypt]"
    
Install libraries for creating bearer tokens
    pip install "python-jose[cryptography]"

to test generated tokens, use https://jwt.io/

install alembic
    pip install alembic

    help
        alembic --help
    init
        alembic init alembic   #second alembic is directory,  creates elembic folder and alembic.ini file
        edit alembic\env.py to add DB call
        edit alembic.ini to sqlalchemy.url
    deply DB    
        alembic revision -m "create posts table"  #creates post table  find version, edit
    find current version
        alembic current
    deployalembic revision -m "create posts table"
        alembic upgrade {revision numner}    #get from revision file
    get the head version, this is the newest versioin
        alembic heads
    to upgrate to head version
        alembic upgrade head
    to see alembic history
        alembic history 
    to autogenerate based on model
        alembic revision --autogenerate -m "some name here"

    
CORS setup
    command to look at browser call
        fetch('http://localhost:8000/').then(res => res.json()).then(console.log)
    search cors in fast api for documentation
        import libraries for middleware
        set app to middleware
    
Note:  to install all requirements in the requirements.txt file
    pip install -r requirements.txt
    pip install -r requirements-windows.txt   

github setup
    git init
    git add --all
    git commit -m "initial commit"
    git config --global user.email ajmvfr@gmail.com
    git config --global user.name ajmvfr
    git commit -m "initial commit"
    git branch -M main
    git remote add origin https://github.com/ajmvfr/WeatherAPI.git
    git remote change origin https://github.com/ajmvfr/WeatherAPI.git
    git push -u origin main

setup heroku for deploying api
    google heroku python the lint to setup and download installer
    intall
    heroku --version     #use this to test
    heroku login
    heroku create fastapi-ajmvfr     #this is a unique name

Digital ocean 
    using terminal ssh to digital ocean
        ssh root@174.138.82.50
        "yes" to fingerprint
        enter password
    update virtual machine
        sudo apt update && sudo apt upgrade -y
    check python version
        python3 --version
    see if pip is installed
        pip --version
    if pip not installed, install intall intall intall
        sudo apt install python3-pip
    use pip to install virtual env
        --old  sudo pip3 install virtualenv
        sudo apt install python3-venv
    install postgres
        sudo apt install postgresql postgresql-contrib -y
    test postgres to access local instand of postgress on server
        psql --version
    see all users on ubunto machine
        sudo cat /etc/passwd
    change to postgress user
        su - postgres
    run local postgres  
        psql -U postgres
    assign password to postgres user
        \password postgres
    exit out of postgres terminal
        \q
    to get back to root user
        exit
    change to postgres directory for more config
        cd /etc/postgresql/12/main   #could be version specific
        update postgresql.conf
            sudo vi postgresql.conf    #add ip address for connect
            sudo vi pg_hba.conf  
                    changed peer log to md5
                    changed ip to allow all ip's
        restart postgres to have changes take effect
            systemctl restart postgresql
    create new user so root is not used
        adduser ajm
        su - ajm    #to login
    or to login as correct user 
        ssh ajm@138.197.36.167
    give user root permissions
        usermod -aG sudo ajm
    test permission using apt upgrade, it should work
        sudo apt upgrade
    to get current directory
        pwd
    to go to home directory
        cd ~
        cd /home/ajm
    Install app
        mkdir weather-api-fastapi
        cd weather-api-fastapi
        virtualenv venv      #make virtual enviroment
        ls -la               #to see folder
        source venv/bin/activate   # to activate enviroment
        deactivate                 # to leave virtual enviroment
        mkdir src                  # make source directory
        cd src                     # change to dir
    pull code onto vm from github
        git clone https://github.com/ajmvfr/WeatherAPI.git .  #make user of space dot to install in current dir
    activate code
        cd ..   to get back to root of app
        source venv/bin/activate   # to activate enviroment
        cd src
        cat requirements.txt   # do this to see requirements
        pip install -r requirements.txt   #install all requirements
    handle error from missing library
        deactivate  # get out of virtual enviroment
        #find library in error and lookup install
        sudo apt install libpq-dev     #this is the issue from this install
        source venv/bin/activate    # back into virtual enviroment
        pip install -r requirements.txt   #try again
    start application
        uvicorn app.main:app    #same as on pc
    create enviroment variables
        export varname=variables  #to set
        unset varname   #to remove
    to see enviroment variables
        printenv 
    to set them in batch
        cd ~ #get back to root
        touch .env  #create empty file  Do not put this in app directory
        vi .env  to maually to it, it uses export as above
        source .env # to set variables
    to set env variables from a copy of local .env file
        #paste in varables from .env local
        set -o allexport; source /home/ajm/.env; set +o allexport
        vi .profile #this makes the env variables autorun
        sudo reboot  #reboot machine or close terminal
    to deploy db table
        source venv/bin/activate #start virtual server
        cd fastapi  #app dir
        cd src/alembic/versions to see versions
        alembic upgrade head to deploy tables
    start app
        # change to source dir of app
        uvicorn --host 0.0.0.0 app.main:app  #adding host to listen to all ip's
        #this is installed and running, but will not autostart
    install gunicorn process manager to allow auto start
        pip install gunicorn  # can be put in requirements.txt file
            might need additional requirements based on errors
                pip install httptools
                pip install uvloop
        gunicorn  -w 1 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 
        # if it will not start with connect error, 
            sudo fuser -k 8000/tcp
    start the process on reboot and in the background
        cd /etc/systemd/system/
        sudo vi weather-api-fastapi.service
        #paste in code from the ervice file
        To test
            systemctl start weather-api-fastapi #or systemctl restart weather-api-fastapi
            systemctl status weather-api-fastapi
        to set to auto restart
            sudo systemctl enable weather-api-fastapi
    Configure NGINX to front end the server, works as a proxy to allow the ssl termination, and pass http to app.
        install
            sudo apt install nginx -y
        to start
            systemctl start nginx
                you can see default page if using bareserver ip without port
        to see sites available 
            cd /etc/nginx/sites-available
            cat default # to see detaults
        look it nginx file in project
            #edit default and load lines in
            sudo vi default
            systemctl restart nginx
        to look for errors
            sudo cat /var/log/nginx/error.log
        verify nginx is will restart on boot
            systemctl status nginx
    setting up ssl
        got to https://certbot.eff.org/
        #go to certbot instructions
        #pick nginx on ubuntu 20 
        #follow instructions
        #verify snapd is installed
            snap --version
        #install cetbot
            sudo snap install --classic certbot
        #run certbot to congif nginx
            sudo certbot --nginx

        cert created for anthonymorgan.us www.anthonymorgan.us api.anthonymorgan.us

    setup firewall
        #will use the builtin firewall called ufw
        #check it
            sudo ufw status
        #setup firewall rules
            sudo ufw allow http     
            sudo ufw allow https
            sudo ufw allow ssh     #allow remote access
            sudo ufw allow 5432    #allow remote admin for DB
            sudo ufw enable     #start firewall
Pushing changes with github
    #make changes to code and save changes
    #command line   
        git add --all
        git commit -m "New Code to test deploy"
        git push origin main
        #terminal service to vm
        #change dir to source folder
        #restart app
        sudo systemctl restart weather-api-fastapi
Testing tooling
    #search for pytest
    install pytest
        pip install pytest
        pytest -v  #for verbose
        pytest -v -s #for verbose and display print startments
        pytest -v -s tests\test_users.py
        pytest -v -s tests\test_users.py --disable-warnings -x   # -x stop at first error
        pytest --disable-warnings
        pytest -v -s --disable-warnings -x

