# Standard Library Imports
import logging
import sys

# Related Third Party Imports
import boto
from boto.route53.connection import Route53Connection

# Boto logging
boto.set_stream_logger('boto')

# Set up connection
HOSTED_ZONE = 'Z91M68L2BIK7T'
DOMAIN_NAME = 'testing.com'

# Set up logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('dyndns_route53.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def main():

    conn = Route53Connection()

    try:
        print "tried!!!"
        zone = conn.get_hosted_zone(HOSTED_ZONE)
        print "it works!"
        print zone
    except:
        print "shit is broken. fix your shit"
        logger.error('%s Zone Not Found' % HOSTED_ZONE)
        sys.exit(1)

    response = conn.get_all_rrsets(HOSTED_ZONE, 'A', DOMAIN_NAME, maxitems=1)[0]
    print "before response"
    print response
    print "post response"

    changes = "nothing"
    #new_change = ResourceRecordSet(conn, HOSTED_ZONE, '')
    #change1 = new_change('CREATE', DOMAIN_NAME, 'A', response.ttl)

    try:
        commit = changes.commit()
        logger.debug('%s' % commit)
    except:
        logger.error("Changes can't be made: %s" % commit)
        sys.exit(1)


if __name__ == '__main__':
    main()

