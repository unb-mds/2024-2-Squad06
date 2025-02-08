import React, { useState } from 'react';

interface CardGastoProps {
  className?: string;
  nomeFornecedor: string;
  cnpjFornecedor: string;
  valorMensal: number;
  valorAnual: number;
  dataAssinatura: string;
  periodoVigencia: string;
  dataPublicacao: string;
}

function CardGasto({ 
  className = '', 
  nomeFornecedor, 
  cnpjFornecedor, 
  valorMensal, 
  valorAnual, 
  dataAssinatura, 
  periodoVigencia, 
  dataPublicacao 
}: CardGastoProps) {
  const [expandido, setExpandido] = useState(false);
  const handleClick = () => setExpandido(!expandido);

  return (
    <div className={`bg-[#112632] rounded-lg shadow-md p-5 text-center my-5 ${className}`}>
      <h2 className="text-xl text-white">{nomeFornecedor}</h2>
      <p className="text-white">CNPJ: {cnpjFornecedor}</p>
      <p className="text-white">Publicação: {dataPublicacao}</p>
      <p className="text-white">Valor Mensal: R$ {valorMensal} | Valor Anual: R$ {valorAnual}</p>
      <p className="text-white">Assinatura: {dataAssinatura}</p>
      <p className="text-white">Vigência: {periodoVigencia}</p>
      <button onClick={handleClick} className="bg-[#EFEFEF] text-black rounded-full py-2 px-6 mt-3">
         {expandido ? "Ocultar Detalhes" : "Ver Detalhes"}
      </button>
      {expandido && (
        <div className="mt-4 text-white">
          <p>Mais detalhes sobre o fornecedor poderão ser exibidos aqui.</p>
        </div>
      )}
    </div>
  );
}

export default CardGasto;
