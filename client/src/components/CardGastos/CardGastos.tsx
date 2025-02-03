import React, { useState } from 'react';

function CardGastos({ 
    className = '', 
    nomeFornecedor = '', 
    cnpjFornecedor = '', 
    periodoVigencia = '', 
    valorMensal = 0, 
    valorAnual = 0, 
    dataAssinatura = '', 
    dataPublicacao = '' 
}) {
    const [expandido, setExpandido] = useState(false);

    const handleClick = () => {
        setExpandido(!expandido);
    };

    return (
        <div className={`bg-[#112632] rounded-lg shadow-md p-[1.25rem] text-center my-[1.25rem] ${className}`}>
            <h2 className="text-xl mb-2.5 text-white">{nomeFornecedor}</h2>
            <div className="flex justify-between items-center gap-2">
                <p className="text-base text-white mb-[0.9375rem] truncate">Publicação: {dataPublicacao}</p>
                <p className="text-base text-white mb-[0.9375rem] truncate">Valor Anual: R${valorAnual}</p>
            </div>
            <div className="w-full h-[0.0625rem] bg-[#dcdcdc] mb-4"></div>
            <p className={`text-sm text-white mb-4 text-justify ${expandido ? 'hidden' : ''}`}>
                O fornecedor {nomeFornecedor} (CNPJ: {cnpjFornecedor}) possui vigência de contrato de {periodoVigencia}, 
                com valor mensal de R$ {valorMensal} e valor anual de R$ {valorAnual}.
            </p>
            <button
                className="bg-[#EFEFEF] text-black text-base border-none rounded-full py-[0.3125rem] px-[4.375rem] cursor-pointer hover:underline"
                onClick={handleClick}
            >
                Ver {expandido ? 'Menos' : 'Mais'}
            </button>
            {expandido && (
                <div className="fixed top-0 left-0 right-0 bottom-0 bg-[#112632] p-6 z-30 overflow-y-auto">
                    <div className="flex flex-col gap-4">
                        <h2 className="text-xl text-white">{nomeFornecedor}</h2>
                        <div className="flex justify-between items-center gap-2 text-white">
                            <p className="text-base">Data de Publicação: {dataPublicacao}</p>
                            <p className="text-base">Valor Anual: R$ {valorAnual}</p>
                        </div>
                        <div className="w-full h-[0.0625rem] bg-[#dcdcdc] mb-4"></div>
                        <p className="text-sm text-white mb-4 text-justify">
                            O fornecedor {nomeFornecedor} (CNPJ: {cnpjFornecedor}) possui vigência de contrato de {periodoVigencia}, 
                            com valor mensal de R$ {valorMensal} e valor anual de R$ {valorAnual}.<br /> 
                            A assinatura ocorreu em {dataAssinatura} e a publicação foi realizada em {dataPublicacao}.
                        </p>
                        <button
                            className="bg-[#EFEFEF] text-black text-base border-none rounded-full py-[0.3125rem] px-[4.375rem] cursor-pointer hover:underline"
                            onClick={handleClick}
                        >
                            Ver {expandido ? 'Menos' : 'Mais'}
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

export default CardGastos;
