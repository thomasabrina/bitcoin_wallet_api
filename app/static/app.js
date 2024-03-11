document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loadTransactions').addEventListener('click', function() {
        loadTransactions();
    });

    document.getElementById('showBalance').addEventListener('click', function() {
        showBalance();
    });

    document.getElementById('createTransfer').addEventListener('click', function() {
        const amountBtc = document.getElementById('amountBtc').value;
        createTransfer(amountBtc).then(response => {
            if (response.ok) {
                document.getElementById('amountBtc').value = ''; // Clear input field
                loadTransactions(); // Reload transactions
                showBalance(); // Update balance
            } else {
                console.error('Transfer creation failed.');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });
});

function loadTransactions() {
    fetch('/transactions')
        .then(response => response.json())
        .then(data => {
            const transactionsList = document.getElementById('transactionsList');
            transactionsList.innerHTML = ''; // Clear current list
            data.forEach(transaction => {
                const item = document.createElement('li');
                item.textContent = `ID: ${transaction.id}, Amount: ${transaction.amount}, Spent: ${transaction.spent}, Created At: ${transaction.created_at}`;
                transactionsList.appendChild(item);
            });
        });
}

function showBalance() {
    fetch('/balance')
        .then(response => response.json())
        .then(data => {
            document.getElementById('balance').textContent = `BTC: ${data.balance_btc}, EUR: ${data.balance_eur}`;
        });
}

function createTransfer(amountBtc) {
    return fetch('/transfer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ amountBtc: amountBtc }),
    })
    .then(response => response.json()) // Convert the response to JSON
    .then(data => {
        if (data.error) {
            alert(data.error); 
        } else {
            document.getElementById('amountBtc').value = ''; // Clear input field
            loadTransactions(); // Reload transactions
            showBalance(); // Update balance
            alert(data.message); // Alert the success message
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}