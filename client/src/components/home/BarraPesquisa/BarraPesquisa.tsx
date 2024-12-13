import React from 'react';
import './BarraPesquisa.css';

function BarraPesquisa() {
  return (
      <div className="search-container">
        <img className="lupa" src="/assets/lupa.png" alt="Lupa" />
        <form action="/" method="GET">
          <input type="text" id="barraPesquisa" placeholder="Pesquise por um gasto" required />
          <input type="submit" id="botaoPesquisa" value="Buscar" />
        </form>
        <img className="filtro" src="/assets/filtro.png" alt="Filtrar" />
      </div>
  );
}

export default BarraPesquisa;