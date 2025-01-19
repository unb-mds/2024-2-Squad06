import React ,{useState}from 'react';

function CardGastos({ className = '' }) {
    const [expandido, setExpandido] = useState(false);

    const handleClick = () => {
        setExpandido(!expandido);
    };

    return (
        <div className={`bg-[#112632] rounded-lg shadow-md p-[1.25rem] text-center my-[1.25rem] ${className}`}>
            <h2 className="text-xl mb-2.5 text-white">Título</h2>
            <div className="flex justify-between items-center gap-2">
                <p className="text-base text-white mb-[0.9375rem] truncate">Status: Regular</p>
                <p className="text-base text-white mb-[0.9375rem] truncate">Data: dd/mm/aaaa</p>
            </div>
            <p className="text-base text-white mb-[0.9375rem] truncate text-left">Valor: R$0.000,00</p>
            <div className="w-full h-[0.0625rem] bg-[#dcdcdc] mb-4"></div>
            <p className={`text-sm text-white mb-4 text-justify ${expandido ? 'hidden' : ''}`}>
                Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos -- Informações sobre os gastos
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
                        <h2 className="text-xl text-white">Título (Expandido)</h2>
                        <div className="flex justify-between items-center gap-2 text-white">
                            <p className="text-base">Status: Regular</p>
                            <p className="text-base">Data: dd/mm/aaaa</p>
                            <p className="text-base">Valor: R$0.000,00</p>
                        </div>
                        <div className="w-full h-[0.0625rem] bg-[#dcdcdc] mb-4"></div>
                        <p className="text-sm text-white mb-4 text-justify">
                            Esta é a nova parte que só aparece quando o cartão está expandido. Aqui você pode colocar mais detalhes ou informações adicionais.
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