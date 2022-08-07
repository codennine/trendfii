const header = document.querySelector('h2');
const isMonthlyReport = header.innerText.includes('Mensal');
const isQuarterlyReport = header.innerText.includes('Trimestral');
const isYearlyReport = header.innerText.includes('Anual');
const [fiiSummaryTable] = document.querySelectorAll('table');
const numberOfStocks = fiiSummaryTable.querySelector('tr:nth-child(3) td:nth-child(4)').innerText;
const isinCode = fiiSummaryTable.querySelector('tr:nth-child(3) td:nth-child(2)').innerText;
const period = fiiSummaryTable.querySelector('tr:nth-child(11) td:nth-child(2)').innerText;

if(isMonthlyReport) {
  const div = document.createElement('div');
  const investorsTable = document.querySelector('table:nth-of-type(2)');
  const numberOfInvestors = investorsTable.querySelector('tr:nth-child(2) td:nth-child(2)').innerText;
  header.style.display = 'none';
  const passiveTable = document.querySelector('table:nth-of-type(5)');
  const incomeToDistribute = passiveTable.querySelector('tr:nth-child(2) td:nth-child(3)').innerText;
  const obligationsForTheAcquisitionOfRealState = passiveTable.querySelector('tr:nth-child(5) td:nth-child(3)').innerText;

  document.body.classList.add('fii-monthly-report');
  div.className = 'fii-report-reader-summary-monthly';
  div.innerHTML = `
    <header style="height: 70px; width: 100%; background-image: linear-gradient(to top right, red, orange);"></header>
    <div class="subheader" style="margin-bottom: 10px; display: flex; justify-content: space-between; padding: 8px 8px; border-bottom: 1px solid #333;">
     <p>Informe Mensal ${isinCode.substr(2, 4)}11</p> 
     <p>Competencia: ${period}</p> 
    </div>

    <div style="display: flex; gap: 8px; justify-content: space-between; padding: 10px 8px">
      <div class="highlight-item">
        <p>${obligationsForTheAcquisitionOfRealState}</p>
        <p>Alavancagem</p>
      </div>

      <div class="highlight-item">
        <p>Value</p>
        <p>Cotistas</p>
      </div>

      <div class="highlight-item">
        <p>Value</p>
        <p>Cotas</p>
      </div>

      <div class="highlight-item">
        <p>${incomeToDistribute}</p>
        <p>A distribuir por cota</p>
      </div>
    </div>
  `;
  header.parentNode.insertBefore(div, header.nextSibling);

  // div.innerHTML = `
  //   <h3>Informações básicas</h3>

  //   <div style="display: flex; gap: 5px;">
  //     <div>
  //       <p>${numberOfInvestors}</p>
  //       <p>Número de Cotistas</p>
  //     </div>

  //     <div>
  //       <p>${numberOfStocks}</p>
  //       <p>Numero de cotas</p>
  //     </div>

  //     <div>
  //       <p>${numberOfStocks}</p>
  //       <p>Valor Patrimonial da cota</p>
  //     </div>
  //   </div>


  //   <h3>Ativo</h3>

  //   <div style="display: flex;">
  //     <div>
  //       <p>Valor em caixa</p>
  //       <p>100</p>
  //     </div>

  //     <div>
  //       <p>Valor investido</p>
  //       <p>100</p>
  //     </div>

  //     <div>
  //       <p>Valor a receber</p>
  //       <p>100</p>
  //     </div>
  //   </div>

  //   <h3>Passivo</h3>
  //   <div style="display: flex;">
  //     <div>
  //       <p>Rendimentos a distribuir</p>
  //       <p>100</p>
  //     </div>

  //     <div>
  //       <p>Alavancagem</p>
  //       <p>div bruta / patrimonio liquido</p>
  //     </div>

  //     <div>
  //       <p>Taxa de administração</p>
  //       <p>100</p>
  //     </div>

  //     <div>
  //       <p>Valor a receber</p>
  //       <p>100</p>
  //     </div>
  //   </div>
  // `;

  // https://site.tc.com.br/blog/fundos/informe-mensal-dos-fiis
}

if(isQuarterlyReport) {
  // chrome.runtime.sendMessage('load css');
}
