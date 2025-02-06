import React, { useState, useEffect } from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import { fetchSuppliers, fetchFornecedorByName, fetchDiariosPorFornecedor } from '../../service/api';
import { Fornecedor } from '../../models/Fornecedor';
import { Diario } from '../../models/Diario';
import CardGastos from '../../components/CardGastos/CardGastos';
import LoadingModal from '../../LoadingModal/LoadingModal';

function Filtragem() {
  const [suppliers, setSuppliers] = useState<Fornecedor[]>([]);
  const [selectedSupplier, setSelectedSupplier] = useState<Fornecedor | null>(null);
  const [diarios, setDiarios] = useState<Diario[]>([]);
  const [loadingSuppliers, setLoadingSuppliers] = useState<boolean>(false);
  const [loadingDiarios, setLoadingDiarios] = useState<boolean>(false);
  
  const [filtroDataPublicacao, setFiltroDataPublicacao] = useState<string>('');
  const [filtroDataAssinatura, setFiltroDataAssinatura] = useState<string>('');
  const [modalAberto, setModalAberto] = useState<boolean>(false);
  
  const [page, setPage] = useState<number>(1);

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
    setPage(1);
  };

  const abrirModal = () => setModalAberto(true);
  const fecharModal = () => setModalAberto(false);

  const executarFiltragem = async (pageParam: number) => {
    setLoadingDiarios(true);
    try {
      let supplierId = 0;
      let nome = "";
      if (selectedSupplier) {
        nome = selectedSupplier.nome;
        const result = await fetchFornecedorByName(nome);
        supplierId = result.id;
      }
      const bodyParams = {
        nome,
        data_publicacao: filtroDataPublicacao,
        data_assinatura: filtroDataAssinatura,
        page: pageParam
      };
      const diariosData = await fetchDiariosPorFornecedor(supplierId, bodyParams);
      setDiarios(diariosData);
      console.log("Diários filtrados (página " + pageParam + "):", diariosData);
    } catch (error) {
      console.error("Erro ao filtrar diários:", error);
    } finally {
      setLoadingDiarios(false);
    }
  };

  const handleFiltrarDiarios = async () => {
    setPage(1);
    await executarFiltragem(1);
  };

  const mudarPagina = async (novaPagina: number) => {
    setPage(novaPagina);
    await executarFiltragem(novaPagina);
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
        <div className="flex flex-wrap gap-4 mt-4">
          <button
            onClick={handleFiltrarDiarios}
            className="bg-blue-500 text-white py-2 px-6 rounded hover:bg-blue-700 transition-all"
            disabled={loadingDiarios}
          >
            Buscar Diários
          </button>
          <button
            onClick={abrirModal}
            className="bg-blue-500 text-white py-2 px-6 rounded hover:bg-blue-700 transition-all"
          >
            Filtros Avançados
          </button>
        </div>
      </div>

      {modalAberto && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-80">
            <h3 className="text-lg font-bold mb-4">Filtros Avançados</h3>
            <div className="mb-4">
              <label className="block mb-1 font-medium">Data de Publicação</label>
              <input
                type="date"
                value={filtroDataPublicacao}
                onChange={(e) => setFiltroDataPublicacao(e.target.value)}
                className="w-full p-2 border rounded"
              />
            </div>
            <div className="mb-4">
              <label className="block mb-1 font-medium">Data de Assinatura</label>
              <input
                type="date"
                value={filtroDataAssinatura}
                onChange={(e) => setFiltroDataAssinatura(e.target.value)}
                className="w-full p-2 border rounded"
              />
            </div>
            <div className="flex justify-end gap-2">
              <button
                onClick={fecharModal}
                className="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600 transition-all"
              >
                Cancelar
              </button>
              <button
                onClick={() => {
                  fecharModal();
                }}
                className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-all"
              >
                Aplicar
              </button>
            </div>
          </div>
        </div>
      )}

      {loadingDiarios && <LoadingModal message="Buscando diários..." />}

      <div className="max-w-6xl mx-auto p-4">
        {diarios.length > 0 ? (
          <>
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
            <div className="flex justify-center mt-4 items-center space-x-4">
              {page > 1 && (
                <button 
                  onClick={() => mudarPagina(page - 1)}
                  className="px-4 py-2 bg-white text-blue-500 border border-blue-500 rounded"
                >
                  Anterior
                </button>
              )}
              <span className="text-gray-700 font-medium">Página {page}</span>
              <button 
                onClick={() => mudarPagina(page + 1)}
                className="px-4 py-2 bg-blue-500 text-white rounded"
              >
                Próxima
              </button>
            </div>
          </>
        ) : (
          !loadingDiarios && (
            <p className="text-center text-bold text-black text-2xl">
              {selectedSupplier
                ? "Nenhum diário encontrado para os filtros selecionados."
                : "Escolha um fornecedor ou utilize os filtros avançados para buscar todos os diários."}
            </p>
          )
        )}
      </div>
      <Footer />
    </div>
  );
}

export default Filtragem;
