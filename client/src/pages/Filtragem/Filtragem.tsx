import React from 'react';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';
import BarraPesquisa from '../../components/home/BarraPesquisa/BarraPesquisa';
import BarraFiltragem from '../../components/home/BarraFiltragem/BarraFiltragem';
import CardGasto from '../../components/CardGastos/CardGastos';

function Filtragem() {
    return (
        <div>
            <Header />
            <div className="mt-5">
                <BarraPesquisa />
            </div>
            <div className="mt-5 flex">
                {/* Barra de Filtragem */}
                <div className="w-64 top-24 left-4">
                    <BarraFiltragem />
                </div>
                {/* Cards de Gastos à direita da Barra de Filtragem */}
                <div className="ml-20 w-[600rem] flex flex-col gap-4">
                    <CardGasto />
                    <CardGasto />
                    <CardGasto />
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Filtragem;