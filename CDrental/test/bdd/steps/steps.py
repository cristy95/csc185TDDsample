from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp

from cd_app import app

from customer_list import Customer_list
from customer import Customer
from cd_list import CDList
from cd import CD
from checkout import Checkout
from cd_rental import CD_rental

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
	world.browser = TestApp(app)
	world.response = world.browser.get('http://localhost:5000/')
	assert_equal(world.response.status_code, 200)

@step(u'customer has an identification "([^"]*)" and CD has an identity "([^"]*)"')
def customer_has_an_identification_group1_and_CD_has_an_identity_group2(step,customer_id, cd_id):
	customer_list1 = Customer_list()
	cd_list1 = CDList()
	cd_rent = CD_rental()
	customer1 = Customer(customer_id, "Kringot")
	cd1 = CD(cd_id, "Unrented")
	customer_list1.add_customer(customer1)
	cd_list1.add_cd(cd1)
	checkout1 = Checkout(customer1.customer_id, customer1.name, cd1.cd_id, "11/25/14", "11/27/14")
	cd_rent.add_checkout(checkout1)

@step(u'When I enter the customer identification "([^"]*)" and CD identifier "([^"]*)"')
def when_i_enter_customer_identification_group1_and_cd_identifier_group2(step, customer_id, cd_id):
	form = world.response.forms['rental-form']
	form['customer_id'] = customer_id
	form['cd_id'] = cd_id
	world.form_response = form.submit()
	assert_equal(world.form_response.status_code, 200)
	

@step(u'Then CD is recorded as rented')
def then_cd_is_recorded_as_rented(step):
	cd_list1 = CDList()
	cd1 = CD("Beatles", "Unrented")

	assert_equal(cd1.cd_status, "Unrented")

	cd1.change_status()
	assert_equal(cd1.cd_status, "Rented")

@step(u'Rental contract is printed')
def rental_contract_is_printed(step):
	customer_list1 = Customer_list()
	cd_list1 = CDList()
	customer1 = Customer("001", "Kringot")
	cd1 = CD("Beatles", "Rented")
	checkout1 = Checkout(customer1.customer_id, customer1.name, cd1.cd_id, "11/25/14", "11/27/14")
	cd_rent = CD_rental()

	cd_rent.add_checkout(checkout1)
	ans = cd_rent.get_checkout_record(checkout1)

	assert_equal(ans.customer_id, "001")