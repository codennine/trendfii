const header = document.querySelector('h2');
const isMonthlyReport = header.innerText.includes('Mensal');
const isQuarterlyReport = header.innerText.includes('Trimestral');
const isYearlyReport = header.innerText.includes('Anual');
const [fiiSummary] = document.querySelectorAll('table');
const numberOfStocks = fiiSummary.querySelector('tr:nth-child(3) td:nth-child(4)').innerText;

if(isQuarterlyReport) {
  // chrome.runtime.sendMessage('load css');
}

if(isMonthlyReport) {
  const div = document.createElement('div');
  const investorsTable = document.querySelector('table:nth-of-type(2)');
  const numberOfInvestors = investorsTable.querySelector('tr:nth-child(2) td:nth-child(2)').innerText;

  div.className = 'fii-report-reader-summary-monthly';
  div.innerHTML = `
    <h3>Informações básicas</h3>

    <div style="display: flex; gap: 5px;">
      <div>
        <p>${numberOfInvestors}</p>
        <p>Número de Cotistas</p>
      </div>

      <div>
        <p>${numberOfStocks}</p>
        <p>Numero de cotas</p>
      </div>

      <div>
        <p>${numberOfStocks}</p>
        <p>Valor Patrimonial da cota</p>
      </div>
    </div>


    <h3>Ativo</h3>

    <div style="display: flex;">
      <div>
        <p>Valor em caixa</p>
        <p>100</p>
      </div>

      <div>
        <p>Valor investido</p>
        <p>100</p>
      </div>

      <div>
        <p>Valor a receber</p>
        <p>100</p>
      </div>
    </div>

    <h3>Passivo</h3>
    <div style="display: flex;">
      <div>
        <p>Rendimentos a distribuir</p>
        <p>100</p>
      </div>

      <div>
        <p>Alavancagem</p>
        <p>div bruta / patrimonio liquido</p>
      </div>

      <div>
        <p>Taxa de administração</p>
        <p>100</p>
      </div>

      <div>
        <p>Valor a receber</p>
        <p>100</p>
      </div>
    </div>
  `;

  header.parentNode.insertBefore(div, header.nextSibling);
}
