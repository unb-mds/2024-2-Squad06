import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/BarraPesquisa/BarraPesquisa';
import CardGasto from '../../components/CardGastos/CardGastos'
import Carrossel from '../../components/carrossel/carrosel';
import './Home.css';
function Home() {
  return (
    <div className="Home">
      <Header />
      <Carrossel/>
      <BarraPesquisa />
      <div className='Cards'>
        <CardGasto />
        <CardGasto />
        <CardGasto />
      </div>

      <Footer />
    </div>
  );
}

export default Home;
