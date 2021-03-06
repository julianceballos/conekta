#!/usr/bin/python
# coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import unittest

from conekta import Conekta

# credentials
PUBLIC_KEY = 'XHj7GsiJaWBy3Zgkj93z'
PRIVATE_KEY = ''


class BaseEndpointTestCase(unittest.TestCase):

    api = Conekta(PUBLIC_KEY, PRIVATE_KEY)

    card_charge_object = {
        "amount": 10000,
        "currency": "MXN",
        "description": "DVD - Zorro",
        "customer": {
            "name": "Gilberto Gil",
            "email": "gil.gil@mypayments.mx",
            "phone": 5567942342,
            "street1": "Jiminez 11",
            "street2": "Despacho 99",
            "street3": "La Condesa",
            "city": "Cuauhtemoc",
            "state": "DF",
            "country": "MX",
            "zip": "06100"
        },
        "card": {
            "name": "Gilberto Gil",
            "cvc": "000",
            "number": "4111111111111111",
            "exp_month": "04",
            "exp_year": "16",
            "success_url": "https://www.ftw.com",
            "failure_url": "https://www.epic-fail.com"
        }
    }
    cash_charge_object = {
        "amount": 10000,
        "currency": "MXN",
        "description": "DVD - Zorro",
        "customer": {
            "name": "Gilberto Gil",
            "email": "gil.gil@mypayments.mx",
            "phone": 5567942342,
            "street1": "Jiminez 11",
            "street2": "Despacho 99",
            "street3": "La Condesa",
            "city": "Cuauhtemoc",
            "state": "DF",
            "country": "MX",
            "zip": "06100"
        },
        "cash": {
            "type": "oxxo"
        }
    }
    bank_charge_object = {
        "amount": 10000,
        "currency": "MXN",
        "description": "DVD - Zorro",
        "customer": {
            "name": "Gilberto Gil",
            "email": "gil.gil@mypayments.mx",
            "phone": 5567942342,
            "street1": "Jiminez 11",
            "street2": "Despacho 99",
            "street3": "La Condesa",
            "city": "Cuauhtemoc",
            "state": "DF",
            "country": "MX",
            "zip": "06100"
        },
        "bank": {
            "type": "banorte"
        }
    }
