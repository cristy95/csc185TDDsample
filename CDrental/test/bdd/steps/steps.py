from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp

from cd_app import app

@step(u'customer has an identification')
def customer_has_an_identification(step):
	world.browser = TestApp(app)
	world.response = world.browser.get('http://localhost:5000/')
	assert_equal(world.response.status_code, 200)
	assert_equal(world.response.text, u'OK!')