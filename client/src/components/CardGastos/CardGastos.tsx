import React from 'react';
import './CardGastos.css';


function SobreNos() {
    return (
    <div className="content-block">
        <h2 className="title_box">Título</h2>
        <div className='data_valor'>
            <p className="value_box">data: dd/mm/aaaa</p>
            <p className="value_box">valor: R$0.000,00</p>
        </div>
        <div className="linha_box"></div>
        <p className="content_box">
            Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos
        </p>
        <button className="btn_box">Ver Mais</button>
    </div>
    );
  }

  export default SobreNos;