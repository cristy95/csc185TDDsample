Feature: Check out a CD 
			for a customer

			As a clerk, I want to 
			check out a CD
			for a customer

Scenario: Check out a CD
		Given I visit the homepage
		And customer has an identification "001" and CD has an identity "Beatles"
		When I enter the customer identification "001" and CD identifier "Beatles"
		Then CD is recorded as rented
		Rental contract is printed