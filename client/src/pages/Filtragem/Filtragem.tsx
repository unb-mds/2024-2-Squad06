import React, { useState, useEffect } from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import BarraFiltragem from '../../components/home/BarraFiltragem/BarraFiltragem';
import CardGasto from '../../components/CardGastos/CardGastos';

interface FornecedorData {
    fornecedor: {
        nome: string;
        cnpj: string;
    };
    valores: {
        mensal: number;
        anual: number;
    };
    data_assinatura: string;
    vigencia: string;
}

interface ContratacoesData {
    date: string;
    contratacoes: FornecedorData[];
}


interface Filtros {
    valorMensal: number | null;
    dataPublicacao: string | null;
    dataAssinatura: string | null;
    comparacaoValor: 'maior' | 'menor' | 'igual' | null;
}

function Filtragem() {
    const [fornecedores, setFornecedores] = useState<FornecedorData[]>([]);
    const [dataPublicacao, setDataPublicacao] = useState<string>('');  
    const [currentPage, setCurrentPage] = useState(1); 
    const [itemsPerPage] = useState(3); 

    
    const [filtros, setFiltros] = useState<Filtros>({
        valorMensal: null,
        dataPublicacao: null,
        dataAssinatura: null,
        comparacaoValor: null
    });


    const [filtrosTemporarios, setFiltrosTemporarios] = useState<Filtros>(filtros);

    const [loading, setLoading] = useState(false);

    useEffect(() => {
        setLoading(true);  
        fetch('/teste.json')
            .then((response) => response.json())
            .then((data: ContratacoesData) => {
                setDataPublicacao(data.date);
                const contratacoes = data.contratacoes.sort((a, b) => {
                    return new Date(b.data_assinatura).getTime() - new Date(a.data_assinatura).getTime();
                });
                setFornecedores(contratacoes);
                setLoading(false); 
            })
            .catch((error) => {
                console.error('Erro ao carregar os dados:', error);
                setLoading(false);  
            });
    }, []);

    const aplicarFiltros = (fornecedores: FornecedorData[]) => {
        return fornecedores.filter((fornecedor) => {
            const { valorMensal, dataPublicacao, dataAssinatura, comparacaoValor } = filtros;
    
            
            const filtroValorMensal = valorMensal != null ? (
                comparacaoValor === 'maior' ? fornecedor.valores.mensal > valorMensal :
                comparacaoValor === 'menor' ? fornecedor.valores.mensal < valorMensal :
                comparacaoValor === 'igual' ? fornecedor.valores.mensal === valorMensal :
                true
            ) : true;
    
            
            const filtroDataPublicacao = dataPublicacao ? new Date(fornecedor.data_assinatura) >= new Date(dataPublicacao) : true;
    
            
            const filtroDataAssinatura = dataAssinatura ? new Date(fornecedor.data_assinatura) >= new Date(dataAssinatura) : true;
    
            return filtroValorMensal && filtroDataPublicacao && filtroDataAssinatura;
        });
    };

    const fornecedoresFiltrados = aplicarFiltros(fornecedores);
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = fornecedoresFiltrados.slice(indexOfFirstItem, indexOfLastItem);

    const paginate = (pageNumber: number) => setCurrentPage(pageNumber);
    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(fornecedoresFiltrados.length / itemsPerPage); i++) {
        pageNumbers.push(i);
    }

    const handleAplicarFiltros = () => {
        setLoading(true);  
        setFiltros(filtrosTemporarios); 
        setTimeout(() => {  
            setLoading(false);  
        }, 1200);
    };

    const handleResetFiltros = () => {
        setFiltros({
            valorMensal: null,
            dataPublicacao: null,
            dataAssinatura: null,
            comparacaoValor: null
        });
        setFiltrosTemporarios({
            valorMensal: null,
            dataPublicacao: null,
            dataAssinatura: null,
            comparacaoValor: null
        }); 
        setLoading(true); 
        setTimeout(() => {  
            setLoading(false);  
        }, 1200);
    };

    return (
        <div>
            <Header />
            <div className="mt-5">
                <BarraPesquisa />
            </div>
            <div className="sm:mt-5 mt-0 ml-2 flex flex-col md:flex-row md:justify-center">
                <div className="md:h-screen mt-0 flex flex-col items-center justify-start p-4">
                    {!loading && (
                        <BarraFiltragem 
                            filtros={filtrosTemporarios} 
                            setFiltros={setFiltrosTemporarios} 
                            aplicarFiltros={handleAplicarFiltros}
                            resetarFiltros={handleResetFiltros}
                        />
                    )}
                </div>
                <div className="flex flex-col gap-4 items-center justify-center">
                    {loading ? (
                        <div className="flex justify-center items-center space-x-2">
                            <div className="w-8 h-8 border-4 border-t-4 border-blue-500 border-solid rounded-full animate-pulse scale-110"></div>
                            <span className="text-lg text-blue-500 ">Carregando...</span>
                        </div>
                    ) : fornecedoresFiltrados.length === 0 ? (
                        <p className="mr-1 text-xl text-red-500">Nenhum fornecedor encontrado com os filtros aplicados.</p>
                    ) : (
                        currentItems.map((fornecedorData, index) => (
                            <CardGasto
                                key={index}
                                className="mt-0 transition-all duration-700 max-w-[95%] md:max-w-[75%]"
                                nomeFornecedor={fornecedorData.fornecedor.nome}
                                cnpjFornecedor={fornecedorData.fornecedor.cnpj}
                                valorMensal={fornecedorData.valores.mensal}
                                valorAnual={fornecedorData.valores.anual}
                                dataAssinatura={fornecedorData.data_assinatura}
                                periodoVigencia={fornecedorData.vigencia}
                                dataPublicacao={dataPublicacao}
                            />
                        ))
                    )}
                    
                    {fornecedoresFiltrados.length > itemsPerPage && !loading && (
                        <div className="flex justify-center mt-0 mb-2 pl-0">
                            <ul className="flex gap-2 pl-0">
                                {pageNumbers.map((number) => (
                                    <li key={number}>
                                        <button
                                            className={`px-4 py-2 border rounded ${currentPage === number ? 'bg-blue-500 text-white' : 'bg-white text-blue-500'}`}
                                            onClick={() => paginate(number)}
                                        >
                                            {number}
                                        </button>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Filtragem;
