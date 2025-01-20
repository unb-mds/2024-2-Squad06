import React, { useState } from 'react';

const BarraFiltragem: React.FC = () => {
    const [expandido, setExpandido] = useState(false);
    const [data, setData] = useState<string>('');
    const [valor, setValor] = useState<number>(0);
    const [usoInput, setUsoInput] = useState<boolean>(false);

    const handleClick = () => {
        setExpandido(!expandido);
    };

    const handleDataChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setData(e.target.value);
    };

    const handleValorChangeRange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setValor(Number(e.target.value));
    };

    const handleValorChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
        setValor(Number(e.target.value));
    };

    const formatarValor = (valor: number) => {
        return valor.toLocaleString('pt-BR', {
            style: 'currency',
            currency: 'BRL',
        });
    };

    return (
        <div className="relative w-[20rem] h-full md:h-[35rem] px-4 bg-gray-300 rounded-lg shadow-md">
            <button
                className="block md:hidden w-full py-2 bg-[#112632] text-white rounded-lg mt-2 hover:bg-[#112632] transition-colors duration-500"
                onClick={handleClick}
            >
                {expandido ? 'Ocultar Filtros' : 'Filtrar'}
            </button>
            <div
                className={`mt-4 ${expandido ? 'block' : 'hidden'} md:block`}
            >
                <h3 className="text-lg font-semibold mb-4">Filtros</h3>
                <div className="mb-4">
                    <label className="block text-sm font-medium">Situação:</label>
                    <select className="w-full mt-1 p-2 border border-gray-300 rounded-lg">
                        <option value="categoria1">Regular</option>
                        <option value="categoria2">Irregular</option>
                    </select>
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium">Valor:</label>
                    <div className="flex items-center">
                        <input
                            type="range"
                            min="0"
                            max="1000"
                            value={valor}
                            onChange={handleValorChangeRange}
                            className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                        />
                        <span className="ml-4 text-sm">{formatarValor(valor)}</span>
                    </div>
                    
                    <div className="mt-2">
                        <label className="block text-sm font-medium">Ou insira o valor:</label>
                        <input
                            type="number"
                            value={valor}
                            onChange={handleValorChangeInput}
                            className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                        />
                    </div>
                </div>
                <div className="mb-4">
                    <label className="block text-sm font-medium">Data:</label>
                    <input
                        type="date"
                        value={data}
                        onChange={handleDataChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>
                <button
                    className="w-full py-2 bg-[#116FBB] text-white rounded-lg mt-0 hover:bg-[#112632] transition-colors duration-500"
                    onClick={() => {
                        alert('Filtros aplicados!');
                        handleClick();
                    }}
                >
                    Filtrar
                </button>
            </div>
        </div>
    );
};

export default BarraFiltragem;
