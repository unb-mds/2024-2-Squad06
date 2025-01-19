import React from 'react';

const BarraFiltragem: React.FC = () => {
    return (
        <div className="w-64 p-4 bg-gray-300 rounded-lg shadow-md top-24 left-4 z-50 ml-8">
            <h3 className="text-lg font-semibold mb-4">Filtros</h3>
            
            <div className="mb-4">
                <label className="block text-sm font-medium">Categoria:</label>
                <select className="w-full mt-1 p-2 border border-gray-300 rounded-lg">
                    <option value="categoria1">Categoria 1</option>
                    <option value="categoria2">Categoria 2</option>
                    <option value="categoria3">Categoria 3</option>
                </select>
            </div>
            
            <div className="mb-4">
                <label className="block text-sm font-medium">Preço:</label>
                <input
                    type="range"
                    min="0"
                    max="100"
                    className="w-full mt-1 p-2 border border-gray-300 rounded-lg"
                />
            </div>
            
            <button
                className="w-full py-2 bg-[#116FBB] text-white rounded-lg mt-4 hover:bg-[#112632] transition-colors duration-500"
                onClick={() => alert('Filtros aplicados!')}
            >
                Filtrar
            </button>
        </div>
    );
};

export default BarraFiltragem;
