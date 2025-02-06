// src/pages/Home/Home.tsx
import React, { useEffect, useState } from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import Carrossel from '../../components/carrossel/carrosel';
import { fetchDiarios } from '../../service/api';
import { Diario } from '../../models/Diario';
import CardGastos from '../../components/CardGastos/CardGastos';

function Home() {
  const [diarios, setDiarios] = useState<Diario[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    async function loadDiarios() {
      try {
        const data = await fetchDiarios();
        console.log(data);
        setDiarios(data);
      } catch (error) {
        console.error('Erro ao buscar diários:', error);
      } finally {
        setLoading(false);
      }
    }
    loadDiarios();
  }, []);

  return (
    <div>
      <Header />
      <Carrossel />
      <BarraPesquisa />

      {loading && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg shadow-lg p-6">
            <p className="text-xl font-bold">Carregando Diários...</p>
          </div>
        </div>
      )}

      <div className="flex flex-col justify-center items-center m-[1rem_0] 
                      1008:justify-between 1008:items-start 1008:gap-[2vw] 1008:flex-row 1008:flex-wrap 1008:m-[1vw_9vw]
                      1300:justify-center 1300:items-center 1300:gap-[1rem] 1300:m-[2rem_auto] 1300:w-[70rem] 1300:flex-row 1300:flex-wrap">
        {diarios.map((diario) => (
          <CardGastos
            key={diario.id}
            id={diario.id}
            dataPublicacao={diario.data_publicacao}
            excerpts={diario.excerpts}
            contratacoes={diario.contratacoes}
            url={diario.url}
            className="max-h-[25%] my-[1.25rem] max-w-[21.875rem] w-full 1008:max-w-[30%] 1300:w-[400px]"
          />
        ))}
      </div>
      <Footer />
    </div>
  );
}

export default Home;
