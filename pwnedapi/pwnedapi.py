#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Python wrapper for the haveibeenpwned.com api v2

url base api v2 : https://haveibeenpwned.com/api/v2/
"""
import requests
from requests.utils import quote
import re

from exception import NotValidEmail, BreachNotFound, UnvalidParameters



class HaveIBeenPwnedApi(object):
    base_api_url = "https://haveibeenpwned.com/api/v2"
    url_breaches = "{}/breaches".format(base_api_url)
    url_breach = "{}/breach/".format(base_api_url)
    url_dataclasses = "{}/dataclasses".format(base_api_url)
    url_account = "{}/breachedaccount/".format(base_api_url)
    url_paste = "{}/pasteaccount/".format(base_api_url)
    params_check_email = ['truncateResponse', 'domain']

    def __init__(self):
        self.user_agent = "Python-Pwnage-Checker"
        # from regexr
        self.regex_email = re.compile(r"^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@([A-Z|a-z|0-9])+((\.){0,1}[A-Z|a-z|0-9]){2}\.[a-z]{2,3}$")

    def get_breach(self, name):
        """ Get a info about a single breach with her name, you can use
        get_all_breaches_name to get all breaches name"""
        list_all_breaches_name = self.get_all_breaches_name()
        if name not in list_all_breaches_name:
            raise BreachNotFound("The breach was not found in the list of all breaches : {}".format(
                                list_all_breaches_name))
        res = requests.get("{}{}".format(self.url_breach, name))
        return res.json()

    def get_all_dataclasses(self):
        """ Get all different types of record compromised """
        res = requests.get(self.url_dataclasses)
        return res.json()

    def get_all_breaches(self, **params):
        payload = params
        res = requests.get(self.url_breaches, params=payload)
        return res.json()

    def get_all_breaches_name(self):
        """ Get all breaches name """
        breaches = self.get_all_breaches()
        return [b['Name']for b in breaches]

    def get_number_breaches(self):
        """ Get the total number of breaches """
        return len(self.get_all_breaches())

    def check_email(self, email, verbose=True, **params):
        """ Check breaches for an email account """
        if not self.regex_email.match(email):
            raise NotValidEmail("the email passed in argument is not a valid email")
        email = quote(email)
        url_email = "{}{}".format(self.url_account, email)
        payload = params
        try:
            res = requests.get(url_email,params=payload)
            if res.status_code == 404:
                if verbose:
                    print("The account could not be found and has therefore not been pwned")
                return []
            else:
                return res.json()
        except Exception as e:
            print(e)
            return []
    def check_pastebin(self, email, verbose=True):
        """ Check if an email is in a pastebin """
        if not self.regex_email.match(email):
            raise NotValidEmail("the email passed in argument is not a valid email")
        email = quote(email)
        url_paste = "{}{}".format(self.url_paste, email)
        try:
            res =  requests.get(url_paste)
            if res.status_code == 404:
                if verbose:
                    print("The account could not be found on any paste lists")
                return []
            else:
                return res.json()
        except Exception as e:
            print(e)
            # if e.code == 400:
            #     raise NotValidEmail("The email you entered is not valid")
            return []


# if __name__ == "__main__":
#     api = HaveIBeenPwnedApi()
#     print(api.get_all_breaches_name())
#     print(api.get_number_breaches())
#     print("Checking email ericfourrier0@gmail.com: {}".format(api.check_email("ericfourrier0@gmail.com")))
#     print("Checking email tvhmxoleoub@gmail.com : {}".format(api.check_email("tvhmxoleoub@gmail.com")))
#     print(api.get_breach('Adobe'))
#     print(api.check_pastebin("ericfourrier0@gmail.com"))
#     print(api.check_pastebin("tvhmxoleoub@gmail.com"))
    #print(api.get_all_breaches())
