import React, { useState } from 'react';

interface Filtros_padrao {
    valorMensal: number | null;
    dataPublicacao: string | null;
    dataAssinatura: string | null;
    comparacaoValor: 'maior' | 'menor' | 'igual' | null;
}

interface BarraFiltragemProps {
    filtros: Filtros_padrao;
    setFiltros: React.Dispatch<React.SetStateAction<Filtros_padrao>>;
    aplicarFiltros: () => void;
    resetarFiltros: () => void;
}

const BarraFiltragem: React.FC<BarraFiltragemProps> = ({
    filtros,
    setFiltros,
    aplicarFiltros,
    resetarFiltros,
}) => {
    const [expandido, setExpandido] = useState(false);

    const handleValorMensalChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFiltros((prev: Filtros_padrao) => ({ ...prev, valorMensal: parseFloat(e.target.value) }));
    };

    const handleDataPublicacaoChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFiltros((prev: Filtros_padrao) => ({ ...prev, dataPublicacao: e.target.value }));
    };

    const handleDataAssinaturaChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFiltros((prev: Filtros_padrao) => ({ ...prev, dataAssinatura: e.target.value }));
    };

    const handleComparacaoValorChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setFiltros((prev: Filtros_padrao) => ({ ...prev, comparacaoValor: e.target.value as 'maior' | 'menor' | 'igual' | null }));
    };

    const resetarTodosFiltros = () => {
        setFiltros({
            valorMensal: null,
            dataPublicacao: null,
            dataAssinatura: null,
            comparacaoValor: null,
        });
    };

    return (
        <div className="relative w-[20rem] h-full md:h-[35rem] px-4 bg-gray-300 rounded-lg shadow-md">
            <button
                className="block md:hidden w-full py-2 bg-[#112632] text-white rounded-lg mt-2 hover:bg-[#112632] transition-colors duration-500"
                onClick={() => setExpandido(!expandido)}
            >
                {expandido ? 'Ocultar Filtros' : 'Filtrar'}
            </button>
            <div className={`mt-4 ${expandido ? 'block' : 'hidden'} md:block`}>
                <h3 className="text-lg font-semibold mb-4">Filtros</h3>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Valor Mensal:</label>
                    <input
                        type="number"
                        step="0.01"
                        value={filtros.valorMensal ?? ''}
                        onChange={handleValorMensalChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Comparação de Valor:</label>
                    <select
                        value={filtros.comparacaoValor ?? ''}
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
                        value={filtros.dataPublicacao ?? ''}
                        onChange={handleDataPublicacaoChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <div className="mb-4">
                    <label className="block text-sm font-medium">Data de Assinatura:</label>
                    <input
                        type="date"
                        value={filtros.dataAssinatura ?? ''}
                        onChange={handleDataAssinaturaChange}
                        className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                    />
                </div>

                <button
                    className="w-full py-2 bg-[#116FBB] text-white rounded-lg mt-2 hover:bg-[#112632] transition-colors duration-500"
                    onClick={aplicarFiltros}
                >
                    Filtrar
                </button>
                <button
                    className="w-full py-2 bg-[#FF5733] text-white rounded-lg mt-2 hover:bg-[#cc4422] transition-colors duration-500"
                    onClick={() => {
                        resetarTodosFiltros();
                        resetarFiltros();
                    }}
                >
                    Limpar Filtros
                </button>
            </div>
        </div>
    );
};

export default BarraFiltragem;
