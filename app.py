from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_receipt', methods=['POST'])
def generate_receipt():
    name = request.form.get('name')
    date = datetime.datetime.now().strftime('%d/%m/%y')
    time = datetime.datetime.now().strftime('%H:%M')
    item = request.form.get('item')
    quantity = int(request.form.get('quantity'))
    price_per_item = float(request.form.get('price'))

    subtotal = quantity * price_per_item
    cgst = subtotal * 0.025
    sgst = subtotal * 0.025
    total = subtotal + cgst + sgst
    grand_total = round(total)
    round_off = round(total - grand_total, 2)

    return render_template('receipt.html', name=name, date=date, time=time, item=item, quantity=quantity,
                           price_per_item=price_per_item, subtotal=subtotal, cgst=cgst, sgst=sgst,
                           round_off=round_off, grand_total=grand_total)

if __name__ == '__main__':
    app.run(debug=True)
