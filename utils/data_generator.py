#!/usr/bin/env python3
import string
import random


def email_generator(email_type=None):
    """
    :param email_type: None or incorrect
    :return: string with email or string as incorrect email
    """

    domains = ['armyspy.com', 'cuvox.de', 'dayrep.com', 'einrot.com',
               'fleckens.hu', 'gustr.com', 'jourrapide.com', 'rhyta.com',
               'teleworm.us', 'superrito.com']

    s = string.ascii_lowercase[0:15]
    prefix = ''.join(random.sample(s, len(s)))

    if not email_type:
        return '{0}@{1}'.format(prefix, random.choice(domains))
    elif email_type == 'incorrect':
        return '{0}@'.format(prefix)
