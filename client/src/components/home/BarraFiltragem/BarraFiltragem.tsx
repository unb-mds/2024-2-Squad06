import React, { useState } from 'react';

const BarraFiltragem: React.FC = () => {
    const [expandido, setExpandido] = useState(false);
    const [valorMensal, setValorMensal] = useState<number>(0);
    const [valorAnual, setValorAnual] = useState<number>(0);
    const [dataPublicacao, setDataPublicacao] = useState<string>(''); 
    const [dataAssinatura, setDataAssinatura] = useState<string>('');
    const [usoInput, setUsoInput] = useState<boolean>(false);

    const handleClick = () => {
        setExpandido(!expandido);
    };

    const handleDataPublicacaoChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setDataPublicacao(e.target.value);
    };

    const handleDataAssinaturaChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setDataAssinatura(e.target.value);
    };

    const handleValorMensalChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const valor = parseFloat(e.target.value);
        setValorMensal(valor);
        setValorAnual(valor * 12); // Atualiza o valor anual com base no valor mensal
    };

    const handleValorAnualChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const valor = parseFloat(e.target.value);
        setValorAnual(valor);
        setValorMensal(valor / 12); // Atualiza o valor mensal com base no valor anual
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
                    <label className="block text-sm font-medium">Valor Mensal:</label>
                    <input
                        type="number"
                        step="0.01"
                        value={valorMensal}
                        onChange={handleValorMensalChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Valor Anual:</label>
                    <input
                        type="number"
                        step="0.01"
                        value={valorAnual}
                        onChange={handleValorAnualChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Data de Publicação:</label>
                    <input
                        type="date"
                        value={dataPublicacao}
                        onChange={handleDataPublicacaoChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Data de Assinatura:</label>
                    <input
                        type="date"
                        value={dataAssinatura}
                        onChange={handleDataAssinaturaChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>
                <button
                    className="w-full py-2 bg-[#116FBB] text-white rounded-lg mt-0 hover:bg-[#112632] transition-colors duration-500"
                    onClick={() => {
                        alert('Filtros aplicados');
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
