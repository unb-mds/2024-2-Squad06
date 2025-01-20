import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import CardGasto from '../../components/CardGastos/CardGastos'
import Carrossel from '../../components/carrossel/carrosel';
function Home() {
  return (
    <div >
      <Header />
      <Carrossel/>
      <BarraPesquisa />
      <div className="flex flex-col justify-center items-center m-[1rem_0] 
                       1008:justify-between 1008:items-start 1008:gap-[2vw] 1008:flex-row 1008:flex-wrap 1008:m-[1vw_9vw]
                       1300:justify-center 1300:items-center 1300:gap-[1rem] 1300:m-[2rem_auto] 1300:w-[70rem] 1300:flex-row 1300:flex-wrap ">
        <CardGasto className='max-h-[25%] my-[1.25rem] max-w-[21.875rem] w-full 1008:max-w-[30%] 1300:w-[400px]'/>
        <CardGasto className='max-h-[25%] my-[1.25rem] max-w-[21.875rem] w-full 1008:max-w-[30%] 1300:w-[400px]'/>
        <CardGasto className='max-h-[25%] my-[1.25rem] max-w-[21.875rem] w-full 1008:max-w-[30%] 1300:w-[400px]'/>
      </div>

      <Footer />
    </div>
  );
}

export default Home;