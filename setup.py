#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="sangwook",
    version="0.1.0",
    packages=setuptools.find_packages(),
    author="sangwook",
    description="sangwook desc",
    entry_points={
        'neutron.ml2.type_drivers': ['sangwooktype = sangwook.type_sangwook:SangwookTypeDriver'],
        'neutron.ml2.mechanism_drivers': ['sangwookmech = sangwook.mech_sangwook:SangwookMechanismDriver']
    }
)
