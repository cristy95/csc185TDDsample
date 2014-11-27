from flask import Flask, render_template, request
from cd_rental import CD_rental 
from checkout import Checkout
app = Flask(__name__)
CD_RENTAL = CD_rental()

@app.route('/')
def ok():
	customer_id = request.args.get('customer_id')
	cd_id = request.args.get('cd_id')
	checkout1 = Checkout(customer_id, "Kringot", cd_id, "11/25/14", "11/27/14")
	CD_RENTAL.add_checkout(checkout1)
	chec = CD_RENTAL.get_checkout_record(checkout1)
	cd_id1 = chec.cd_id
	print cd_id1
	customer_id1 = chec.customer_id
	name = chec.name
	date_rented = chec.date
	due_date = chec.due_date
	return render_template('index.html', cd_id1=cd_id1, customer_id1=customer_id1, name=name, date_rented=date_rented, due_date=due_date)


if __name__ == '__main__':
	app.run(debug=True)