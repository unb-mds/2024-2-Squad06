// src/pages/Filtragem/Filtragem.tsx
import React, { useState, useEffect } from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import { fetchSuppliers, fetchFornecedorByName, fetchDiariosPorFornecedor } from '../../service/api';
import { Fornecedor } from '../../models/Fornecedor';
import { Diario } from '../../models/Diario';
import CardGastos from '../../components/CardGastos/CardGastos';

function Filtragem() {
  const [suppliers, setSuppliers] = useState<Fornecedor[]>([]);
  const [selectedSupplier, setSelectedSupplier] = useState<Fornecedor | null>(null);
  const [diarios, setDiarios] = useState<Diario[]>([]);
  const [loadingSuppliers, setLoadingSuppliers] = useState<boolean>(false);
  const [loadingDiarios, setLoadingDiarios] = useState<boolean>(false);

  useEffect(() => {
    setLoadingSuppliers(true);
    fetchSuppliers()
      .then((data) => {
        setSuppliers(data);
        setLoadingSuppliers(false);
      })
      .catch((error) => {
        console.error("Erro ao buscar fornecedores:", error);
        setLoadingSuppliers(false);
      });
  }, []);

  const handleSupplierChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const supplierNome = e.target.value;
    const supplier = suppliers.find(s => s.nome === supplierNome) || null;
    setSelectedSupplier(supplier);
  };

  const handleFiltrarDiarios = async () => {
    setLoadingDiarios(true);
    if (!selectedSupplier) {
        try {
            const diariosData = await fetchDiariosPorFornecedor(0, "");
            setDiarios(diariosData);
            console.log("Diários filtrados:", diariosData);
          } catch (error) {
            console.error("Erro ao filtrar diários:", error);
          } finally {
            setLoadingDiarios(false);
          }
      return;
    }
    setLoadingDiarios(true);
    try {
      const { id } = await fetchFornecedorByName(selectedSupplier.nome);
      const diariosData = await fetchDiariosPorFornecedor(id, selectedSupplier.nome);
      setDiarios(diariosData);
      console.log("Diários filtrados:", diariosData);
    } catch (error) {
      console.error("Erro ao filtrar diários:", error);
    } finally {
      setLoadingDiarios(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      
      <div className="max-w-4xl mx-auto p-6 bg-[#112632] rounded-lg shadow-md my-6">
        <h2 className="text-2xl font-bold text-white mb-4">Fornecedores frequentes</h2>
        {loadingSuppliers ? (
          <p className="text-white">Carregando fornecedores...</p>
        ) : (
          <div className="space-y-2">
            {suppliers.map((supplier, index) => (
              <div key={index} className="flex items-center gap-2">
                <input
                  type="radio"
                  name="supplier"
                  value={supplier.nome}
                  checked={selectedSupplier?.nome === supplier.nome}
                  onChange={handleSupplierChange}
                  className="h-5 w-5"
                />
                <span className="text-white">
                  {supplier.nome} (Contratações: {supplier.contract_count})
                </span>
              </div>
            ))}
          </div>
        )}
        <button
          onClick={handleFiltrarDiarios}
          className="mt-4 bg-blue-500 text-white py-2 px-6 rounded hover:bg-blue-600 transition-all"
          disabled={loadingDiarios}
        >
          {loadingDiarios ? "Filtrando diários..." : "Filtrar Diários"}
        </button>
      </div>

      <div className="max-w-6xl mx-auto p-4">
        {diarios.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {diarios.map((diario) => (
              <CardGastos
                key={diario.id}
                id={diario.id}
                dataPublicacao={diario.data_publicacao}
                excerpts={diario.excerpts}
                contratacoes={diario.contratacoes}
                url={diario.url}
                className="w-full"
              />
            ))}
          </div>
        ) : (
          (!loadingDiarios && selectedSupplier) && <p className="text-center text-gray-700">Nenhum diário encontrado para o fornecedor selecionado.</p>
        )}
        {(!loadingDiarios && !selectedSupplier) && <p className="text-center text-gray-700">Escolha um fornecedor ou apenas busque para ter todos diários</p>}
      </div>
      <Footer />
    </div>
  );
}

export default Filtragem;
