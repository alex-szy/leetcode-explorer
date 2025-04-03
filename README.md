# LeetCode Explorer

This is a lightweight static website which presents all your leetcode solutions in a searchable, pretty format. It uses a jinja2 template to render all your problems and solutions on a statically generated website. The magic happens in scripts/generate_site.py, which reads all your solution files in the solutions folder and populates the website with the corresponding entries.

There is a format to be followed in order for the problem set's metadata to be parsed correctly. For best results, when starting on a new problem, simply run the `new_solution.py` script and paste in the url of the leetcode problem, the script will automatically generate the solution file for you.

## Setup

The static site generator needs `jinja2` to work, and the solution file generator needs `requests` to work. Create a virtual environment and install the dependencies:

```
pip install -r requirements.txt
```

## Development

It is entirely optional, but you can install nodemon using npm, which enables you to run the dev script `dev.sh`. This starts a daemon which watches for changes to the files, regenerates the site and hosts it all at once so you don't have to. If you don't use this, simply run the `generate_site.py` script yourself and host the `build` directory yourself as well.

```
npm i -g nodemon
./dev.sh
```

## Deployment

**TODO**
explain github actions and the required setup steps
