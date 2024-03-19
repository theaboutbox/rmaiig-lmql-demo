# RMAIIG LMQL Demo

> Demo code for the March 19, 2024 RMAIIG Engineering Meetup

This project contains some simple examples of using LMQL to constrain
output from LLMs.

## Getting started

0. **Define required environment variables** - These examples assume
   that OPENAI_API_KEY contains a valid OpenAI API Key, and that CMAKE_ARGS
   is configured properly to build llama-cpp-python. If you have your shell
   configured to use `.env` files, adapt `env-example`. 

0. **Install required packages** - Run `poetry install` to install all of
   the software packages required to run the demos.

0. **Test LMQL Installation** - Run `lmql playground` and try some of the
   examples on the web page that comes up to ensure that everything is installed
   and configured correctly.

0. **Launch Notebooks** - Open the notebooks in your Jupyter Notebook editor of
   choice. Note that the last three notebooks will download and install some
   model files locally, requiring about 10GB of space total.