// src/components/CardGastos/CardGastos.tsx
import React, { useState } from 'react';
import { Contratacao } from '../../models/Contratacao';

interface CardGastosProps {
  id?: number;
  dataPublicacao?: string;
  excerpts?: string;
  contratacoes?: Contratacao[];
  url?: string; // Link para baixar o diário
  className?: string;
}

function CardGastos({ id, dataPublicacao, excerpts, contratacoes, url, className = '' }: CardGastosProps) {
  const [expandido, setExpandido] = useState(false);

  const handleOpen = () => setExpandido(true);
  const handleClose = () => setExpandido(false);

  return (
    <div className={`bg-[#112632] rounded-lg shadow-md p-5 text-center my-5 ${className}`}>
      <h2 className="text-xl text-white">
        Diário {id} - {dataPublicacao}
      </h2>
      <p className="text-white truncate">{excerpts}</p>
      <button 
        onClick={handleOpen} 
        className="bg-[#EFEFEF] text-black rounded-full py-2 px-6 mt-3"
      >
        Ver Mais
      </button>

      {expandido && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-[#112632] rounded-lg shadow-lg p-6 w-[80vw] max-w-4xl max-h-[80vh] overflow-auto relative">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl text-white">Detalhes do Diário {id}</h2>
              <button 
                onClick={handleClose} 
                className="bg-[#EFEFEF] text-black rounded-full px-4 py-2"
              >
                Fechar
              </button>
            </div>
            <p className="text-white mb-4">Data de Publicação: {dataPublicacao}</p>
            {contratacoes && contratacoes.length > 0 ? (
              contratacoes.map((contratacao) => (
                <div key={contratacao.id} className="mb-4 border-b border-gray-500 pb-2">
                  <p className="text-white">
                    Contratação {contratacao.id}: R$ {contratacao.valor_mensal} / R$ {contratacao.valor_anual}
                  </p>
                  <p className="text-white">
                    Data de Assinatura: {contratacao.data_assinatura}
                  </p>
                  {contratacao.vigencia && (
                    <p className="text-white">Vigência: {contratacao.vigencia}</p>
                  )}
                </div>
              ))
            ) : (
              <p className="text-white">Sem contratações relevantes</p>
            )}
            {url && (
              <div className="mt-4">
                <a
                  href={url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="bg-[#EFEFEF] text-black rounded-full py-2 px-6 inline-block"
                >
                  Baixar Diário
                </a>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default CardGastos;
