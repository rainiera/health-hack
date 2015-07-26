# HealthCruncher  
athenahealth hackathon 2015

## Development  
- No specific git flow because roles are compartmentalized (web devs are pair programming)
- Chrome does not cooperate with `0.0.0.0`, so `run` config is `(debug=True)`

## Deployment  
- It is an IP address.  
- In `/var/www/healthcruncher`, `run` config is `(host='0.0.0.0', port=8080, debug=True)`
- `$ python api.py` or `$ python main.py` (TBD)

## How to set up development environment (no virtualenvs)

- I assume you have `homebrew`  
- Go to your terminal  
- `cd` into your `dev` directory (if you don't have one, make one!!)  
- This command puts the source of the starter app (this repo) in the directory you're in.  
`$ git clone https://github.com/rainiera/health-hack.git`  
- This command installs a Python other than the Python installed on your system (which Mac OSX uses, and you don't really want to mess with). Also installs `pip`, which stands for "pip installs packages" (get it???).  
`$ brew install python`  
- Check that you're on the right Python:   
`$ which -a python`  
- The the first line in the output should be:  
`/usr/local/bin/python`
- If not, tell me!!!  
- This command installs the Python libraries you need to make the web app. (Think `.jar` files in Java/libraries to imports)
`$ pip install -r requirements.txt`  
- This command installs Redis  
`$ brew install redis`
- Spin up a redis server on a new terminal tab (Cmd + T) or new terminal window (don't touch it after this!)
`$ redis-server`
- Now you're ready!

-`$ python main.py` to run the webserver on localhost  

## Primary roles
Rainier Ababao - data science/deployment  
Hayley Call - web dev  
Sarah Gorring - web dev  
Shaun Mataire -  iOS  

## Idea (0.1)
A web app that accepts user input on easily accessible patient data and output metrics based on a machine learning algorithm.

Soon... an API to hook up to an iOS app!


