#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Exceptions for our pythons wrapper
"""


class NotValidEmail(Exception):
    """ The email is not valid """
    pass


class BreachNotFound(Exception):
    """ The breach Name is not found """
    pass


class UnvalidParameters(Exception):
    pass
