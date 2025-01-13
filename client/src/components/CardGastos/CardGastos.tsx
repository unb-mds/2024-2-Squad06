import React from 'react';

function CardGastos() {
    return (
    <div className="bg-[#112632] rounded-none shadow-[0_0.25rem_0.5rem_rgba(0,0,0,0.1)] p-[1.25rem] text-center max-h-[25%] my-[1.25rem] max-w-[21.875rem] w-full 1008:max-w-[30%] 1300:w-[400px]">
        <h2 className="text-xl mb-2.5 text-white">Título</h2>
        <div className="flex justify-between items-center gap-2">
            <p className="text-base text-white mb-[0.9375rem]">data: dd/mm/aaaa</p>
            <p className="text-base text-white mb-[0.9375rem]">valor: R$0.000,00</p>
        </div>
        <div className="w-full h-[0.0625rem] bg-[#dcdcdc] mb-4"></div>
        <p className="text-sm text-white mb-4 text-justify">
            Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos
        </p>
        <button className="bg-[#EFEFEF] text-black text-base border-none rounded-full py-[0.3125rem] px-[4.375rem] cursor-pointer hover:underline">
            Ver Mais
        </button>
    </div>
    );
  }

  export default CardGastos;