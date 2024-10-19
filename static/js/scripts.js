function runQuery(queryId) {
    let param = null;
    if (queryId === 1) {
        param = prompt("Enter a word to search in lyrics:");
    }

    fetch('/run-query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query_id: queryId, param: param })
    })
    .then(response => response.json())
    .then(data => {
        displayResult(data, queryId);
    });
}


function displayResult(data, queryId) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ''; // Clear previous results

    const columnHeaders = getColumnHeaders(queryId);

    if (Array.isArray(data) && data.length > 0) {
        const table = document.createElement('table');
        table.className = 'table table-striped';

        // Create the header row
        const thead = table.createTHead();
        const headerRow = thead.insertRow();
        columnHeaders.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });

        // Create the data rows
        const tbody = table.createTBody();
        data.forEach(row => {
            const dataRow = tbody.insertRow();
            Object.values(row).forEach(value => {
                const td = document.createElement('td');
                td.textContent = value;
                dataRow.appendChild(td);
            });
        });

        resultDiv.appendChild(table);
    } else if (typeof data === 'object') {
        // Handle single object response
        const pre = document.createElement('pre');
        pre.textContent = JSON.stringify(data, null, 2);
        resultDiv.appendChild(pre);
    } else {
        // Handle other data types
        resultDiv.textContent = 'No results found';
    }
}

function getColumnHeaders(queryId) {
    switch (queryId) {
        case 1:
            return ['Song Name', 'Artists', 'Countries', 'Popular From', 'To', 'Popularity Index From', 'To'];
        case 2:
            return ['Artists', 'Song Name'];
        case 3:
            return ['Song Count', 'Song List'];
        default:
            return [];
    }
}
