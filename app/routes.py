from flask import Blueprint, jsonify, request
from .models import Transaction
from . import db
from .utils import fetch_eur_to_btc_rate
from flask import Blueprint, jsonify, request, render_template

bp = Blueprint('bp', __name__)  # 'bp' is the name of the Blueprint

@bp.route('/favicon.ico')
def favicon():
    return bp.send_static_file('favicon.ico')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/transactions', methods=['GET'])
def list_transactions():
    transactions = Transaction.query.all()
    transactions_data = [{'id': t.id, 'amount': t.amount, 'spent': t.spent, 'created_at': t.created_at.isoformat()} for t in transactions]
    return jsonify(transactions_data)

@bp.route('/balance', methods=['GET'])
def show_balance():
    unspent_transactions = Transaction.query.filter_by(spent=False).all()
    total_btc = sum(t.amount for t in unspent_transactions)
    eur_to_btc_rate = fetch_eur_to_btc_rate()
    print(f"EUR to BTC Rate: {eur_to_btc_rate}")  # Debugging: Log the rate
    total_eur = total_btc * eur_to_btc_rate if eur_to_btc_rate else 0
    return jsonify({'balance_btc': total_btc, 'balance_eur': total_eur})

@bp.route('/transfer', methods=['POST'])
def create_transfer():
    data = request.json
    amount_btc = data.get('amountBtc', 0)
    try:
        amount_btc = float(amount_btc)
    except ValueError:
        return jsonify({'error': 'Invalid amount provided'}), 400

    if amount_btc < 0.00001:
        return jsonify({'error': 'Transfer amount is too small'}), 400

    unspent_transactions = Transaction.query.filter_by(spent=False).order_by(Transaction.created_at).all()
    total_unspent_btc = sum(t.amount for t in unspent_transactions)

    if total_unspent_btc < amount_btc:
        return jsonify({'error': 'Insufficient balance'}), 400

    spent_amount = 0
    for transaction in unspent_transactions:
        if spent_amount < amount_btc:
            transaction.spent = True
            spent_amount += transaction.amount
        else:
            break

    if spent_amount > amount_btc:
        leftover_amount = spent_amount - amount_btc
        new_transaction = Transaction(amount=leftover_amount, spent=False)
        db.session.add(new_transaction)

    db.session.commit()
    return jsonify({'message': 'Transfer successful'}), 200