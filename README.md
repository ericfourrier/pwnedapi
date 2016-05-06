# pwnedapi
[![Travis-CI Build Status](https://travis-ci.org/ericfourrier/pwnedapi.svg?branch=master)](https://travis-ci.org/ericfourrier/pwnedapi)  ![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-MIT%20License-blue.svg)

## Introduction

pwnedapi is a python wrapper of the https://haveibeenpwned.com api

## Installation
Installation via pip is not available now (*coming soon*)

 1. Clone the project on your local computer.

 2. Run the following command

 	* `$ python setup.py install`

## Usage
the methods of the `HaveIBeenPwnedApi` returns exclusively classes.
### Initialisation

    from pwnedapi import HaveIBeenPwnedApi
    api = HaveIBeenPwnedApi() # initiate the class

### Breaches

    breaches = api.get_all_breaches() # get a list of all breaches
    breaches_names = api.get_all_breaches_name() # get a list of all breaches name
    breach_AshleyMadison = api.get_breach(name='AshleyMadison') # Get one specific
    is_my_email_corrupted = api.check_email(email="obiwan@kenobi@gmail.com") # check if your email is corrupted

### Dataclasses
Return the different types of data classes that are associated with a record in a breach email addresses, passwords,...

    dataclasses = api.get_all_dataclasses()

### Pastes
Return  pastes that contain the given email address

    check_paste = api.check_paste(email="obiwan@kenobi@gmail.com")
