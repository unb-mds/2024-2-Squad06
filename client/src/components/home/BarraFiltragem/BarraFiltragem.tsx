import React, { useState } from 'react';

const BarraFiltragem: React.FC = () => {
    const [expandido, setExpandido] = useState(false);
    const [valorMensal, setValorMensal] = useState<number>(0);
    const [comparacaoValor, setComparacaoValor] = useState<'maior' | 'menor' | 'igual' | null>(null);
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
        const valor = parseInt(e.target.value, 10);
        if (valor >= 0) {
            setValorMensal(valor);
        }
    };

    const handleComparacaoValorChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setComparacaoValor(e.target.value as 'maior' | 'menor' | 'igual' | null);
    };

    const handleLimparFiltros = () => {
        setValorMensal(0);
        setComparacaoValor(null);
        setDataPublicacao('');
        setDataAssinatura('');
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
                        value={valorMensal}
                        onChange={handleValorMensalChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Comparação de Valor:</label>
                    <select
                        value={comparacaoValor ?? ''}
                        onChange={handleComparacaoValorChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    >
                        <option value="">Selecione</option>
                        <option value="maior">Maior</option>
                        <option value="menor">Menor</option>
                        <option value="igual">Igual</option>
                    </select>
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
                    className="w-full py-2 bg-red-500 text-white rounded-lg mt-0 hover:bg-red-800 transition-colors duration-500"
                    onClick={handleLimparFiltros}
                >
                    Limpar Filtros
                </button>

                <button
                    className="w-full py-2 bg-[#116FBB] text-white rounded-lg mt-2 hover:bg-[#112632] transition-colors duration-500"
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
