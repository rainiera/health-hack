# health-hack
athenahealth hackathon 2015

# How to set up development environment (no virtualenvs)

- I assume you have `homebrew`  
- Go to your terminal  
- `cd` into your `dev` directory (if you don't have one, make one!!)  
`$ git clone https://github.com/rainiera/health-hack.git`  
- This command puts the source of the starter app (this repo) in the directory you're in.  
`$ brew install python`  
- This command installs a Python other than the Python installed on your system (which Mac OSX uses, and you don't really want to mess with). Also installs `pip`, which stands for "pip installs packages" (get it???).  
- Check that you're on the right Python:   
`$ which -a python`  
- The the first line in the output should be:  
`/usr/local/bin/python`
- If not, tell me!!!  
`$ pip install -r requirements.txt`  
- This command installs the Python libraries you need to make the web app. (Think `.jar` files in Java/libraries to imports)
- Now you're ready!


## Team
Rainier Ababao  
Hayley Call  
Sarah Gorring  
Shaun Mataire

## Idea (0.1)
A web app that accepts user input on easily accessible patient data and output metrics based on a machine learning algorithm.

Soon... an API to hook up to an iOS app!


