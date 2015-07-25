# health-hack
athenahealth hackathon 2015

# How to set up development environment (no virtualenvs)

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

Your first challenge is to, using and finding patterns in the starter code, to make a bare bones web app that takes user input (height and weight), sends it to a server, and redirects the user to a page that indicates their BMI, and, depending on if their BMI is > or <= 25, says if the BMI is over the healthy average. Don't worry about the design yet, just worry about figuring out how Flask and hitting a backend works.

-Hint, you'll need `$ python main.py` to run the webserver on localhost (type in `localhost` into your browser)

## Team
Rainier Ababao - data science  
Hayley Call - web dev  
Sarah Gorring - web dev  
Shaun Mataire -  iOS  

## Idea (0.1)
A web app that accepts user input on easily accessible patient data and output metrics based on a machine learning algorithm.

Soon... an API to hook up to an iOS app!


